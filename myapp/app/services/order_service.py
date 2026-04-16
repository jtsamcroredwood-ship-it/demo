from decimal import Decimal
from fastapi import Request
from sqlalchemy.orm import Session
from app.services.cart_service import CartService
from app.repositories.product_repo import ProductRepository
from app.repositories.order_repo import OrderRepository
from app.exceptions.domain import EmptyCartError, InsufficientStockError
from app.models.user import User

class OrderService:
    def checkout(self, request: Request, user: User, db: Session):
        cart_service = CartService()
        cart_summary = cart_service.get_summary(request, db)
        
        if not cart_summary.items:
            raise EmptyCartError("Your cart is empty.")

        product_repo = ProductRepository(db)
        order_repo = OrderRepository(db)
        
        # Verify stock and collect reductions to be atomic
        for item in cart_summary.items:
            product = product_repo.get_by_id(item.product_id)
            if not product or product.stock < item.quantity:
                raise InsufficientStockError(f"Not enough stock for {item.name}.")
                
        # Deduct stock
        for item in cart_summary.items:
            success = product_repo.reduce_stock(item.product_id, item.quantity)
            if not success:
                raise InsufficientStockError(f"Failed to reduce stock for {item.name}.")

        # Create order
        order = order_repo.create_order(
            user_id=user.id, 
            total_price=cart_summary.total_price, 
            items=cart_summary.items
        )

        # Clear cart
        request.session["cart"] = {}
        
        return order
