from decimal import Decimal
from pydantic import BaseModel

class CartItem(BaseModel):
    product_id: int
    name: str
    quantity: int
    unit_price: Decimal
    subtotal: Decimal

class CartSummary(BaseModel):
    items: list[CartItem]
    total_price: Decimal
