from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

class OrderItemRead(BaseModel):
    id: int
    product_id: int
    quantity: int
    unit_price: Decimal

    class Config:
        from_attributes = True

class OrderRead(BaseModel):
    id: int
    user_id: int
    total_price: Decimal
    status: str
    created_at: datetime
    items: list[OrderItemRead] = []

    class Config:
        from_attributes = True
