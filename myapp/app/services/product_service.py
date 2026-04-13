# Product service for business logic
from sqlalchemy.orm import Session
from app.repositories.product_repo import ProductRepository
from app.schemas.product import ProductRead

class ProductService:
	def __init__(self, db: Session):
		self.repo = ProductRepository(db)

	def get_all_products(self) -> list[ProductRead]:
		products = self.repo.get_all()
		return [ProductRead.from_orm(p) for p in products]

	def get_product_detail(self, product_id: int) -> ProductRead | None:
		product = self.repo.get_by_id(product_id)
		if product:
			return ProductRead.from_orm(product)
		return None
