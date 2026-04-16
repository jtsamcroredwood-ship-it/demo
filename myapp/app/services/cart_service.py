from fastapi import Request
from sqlalchemy.orm import Session
from app.utils.cart import get_cart_from_session, save_cart_to_session
from app.schemas.cart import CartItem, CartSummary
from app.repositories.product_repo import ProductRepository
from app.exceptions.domain import ProductNotFoundError, InsufficientStockError

class CartService:
    def add(self, request: Request, product_id: int, quantity: int, db: Session):
        repo = ProductRepository(db)
        product = repo.get_by_id(product_id)
        if not product:
            raise ProductNotFoundError(f"Product {product_id} not found.")

        cart = get_cart_from_session(request)
        pid_str = str(product_id)
        current_qty = cart.get(pid_str, 0)
        
        if product.stock < current_qty + quantity:
            raise InsufficientStockError(f"Not enough stock for {product.name}.")

        cart[pid_str] = current_qty + quantity
        save_cart_to_session(request, cart)

    def remove(self, request: Request, product_id: int):
        cart = get_cart_from_session(request)
        pid_str = str(product_id)
        if pid_str in cart:
            del cart[pid_str]
            save_cart_to_session(request, cart)

    def update_qty(self, request: Request, product_id: int, quantity: int, db: Session):
        if quantity <= 0:
            self.remove(request, product_id)
            return

        repo = ProductRepository(db)
        product = repo.get_by_id(product_id)
        if not product:
            raise ProductNotFoundError(f"Product {product_id} not found.")

        if product.stock < quantity:
            raise InsufficientStockError(f"Not enough stock for {product.name}.")

        cart = get_cart_from_session(request)
        cart[str(product_id)] = quantity
        save_cart_to_session(request, cart)

    def get_summary(self, request: Request, db: Session) -> CartSummary:
        cart = get_cart_from_session(request)
        repo = ProductRepository(db)
        
        items = []
        total_price = 0
        
        for pid_str, quantity in cart.items():
            product_id = int(pid_str)
            product = repo.get_by_id(product_id)
            if product:
                subtotal = product.price * quantity
                total_price += subtotal
                items.append(CartItem(
                    product_id=product.id,
                    name=product.name,
                    quantity=quantity,
                    unit_price=product.price,
                    subtotal=subtotal
                ))
                
        return CartSummary(items=items, total_price=total_price)
