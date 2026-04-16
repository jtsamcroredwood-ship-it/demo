import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.db.session import SessionLocal
from app.models.user import User
from app.models.product import Product
from app.models.order import Order
from app.models.order_item import OrderItem
from app.utils.hashing import hash_password

def setup_data(db: Session):
    # Ensure a user exists
    user = db.query(User).filter(User.username == "testuser").first()
    if not user:
        user = User(username="testuser", email="test@example.com", hashed_password=hash_password("password"))
        db.add(user)
    
    # Ensure a product exists
    product = db.query(Product).filter(Product.name == "Test Product").first()
    if not product:
        product = Product(name="Test Product", description="Test", price=10.0, stock=5)
        db.add(product)
        
    db.commit()
    db.refresh(user)
    db.refresh(product)
    
    return user, product

def test_full_checkout_flow():
    client = TestClient(app)
    db_session = SessionLocal()
    try:
        user, product = setup_data(db_session)
        
        # Login
        response = client.post("/login", data={"email": "test@example.com", "password": "password"}, follow_redirects=False)
        assert response.status_code == 303, f"Login failed with {response.status_code}: {response.text}"
        
        # Add to cart
        response = client.post(
            "/cart/add",
            data={"product_id": product.id, "quantity": 2},
            follow_redirects=False # httpx TestClient uses follow_redirects instead of allow_redirects
        )
        assert response.status_code == 303
        
        # View cart and ensure item is there
        response = client.get("/cart")
        assert response.status_code == 200
        assert "Test Product" in response.text
        assert "Total: $20.00" in response.text
        
        # Checkout
        response = client.post("/checkout", follow_redirects=False)
        assert response.status_code == 303
        
        # Verify DB order
        order = db_session.query(Order).filter(Order.user_id == user.id).first()
        assert order is not None
        assert order.total_price == 20.0
        assert order.status == "confirmed"
        
        order_item = db_session.query(OrderItem).filter(OrderItem.order_id == order.id).first()
        assert order_item is not None
        assert order_item.product_id == product.id
        assert order_item.quantity == 2
        
        # Verify stock reduction
        db_session.refresh(product)
        assert product.stock == 3
        
        # Verify cart is empty now
        response = client.get("/cart")
        assert response.status_code == 200
        assert ("cart is currently empty" in response.text or "Total: $0.00" in response.text)
    finally:
        # Cleanup
        db_session.query(OrderItem).delete()
        db_session.query(Order).delete()
        db_session.query(Product).delete()
        db_session.query(User).delete()
        db_session.commit()
        db_session.close()

