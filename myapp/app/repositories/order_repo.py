from decimal import Decimal
from sqlalchemy.orm import Session
from app.models.order import Order
from app.models.order_item import OrderItem
from app.schemas.cart import CartItem

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_order(self, user_id: int, total_price: Decimal, items: list[CartItem]) -> Order:
        order = Order(user_id=user_id, total_price=total_price, status="confirmed")
        self.db.add(order)
        self.db.flush()  # To get order.id

        for item in items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                unit_price=item.unit_price
            )
            self.db.add(order_item)

        self.db.commit()
        self.db.refresh(order)
        return order

    def get_orders_by_user(self, user_id: int) -> list[Order]:
        return self.db.query(Order).filter(Order.user_id == user_id).order_by(Order.created_at.desc()).all()
