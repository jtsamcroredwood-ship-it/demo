# Product repository for DB operations
from sqlalchemy.orm import Session
from app.models.product import Product

class ProductRepository:
	def __init__(self, db: Session):
		self.db = db

	def get_all(self) -> list[Product]:
		return self.db.query(Product).all()

	def get_by_id(self, product_id: int) -> Product | None:
		return self.db.query(Product).filter(Product.id == product_id).first()

	def reduce_stock(self, product_id: int, quantity: int) -> bool:
		product = self.get_by_id(product_id)
		if product and product.stock >= quantity:
			product.stock -= quantity
			self.db.commit()
			return True
		return False
