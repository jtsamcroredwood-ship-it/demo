# ProductRead schema for product output
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

class ProductRead(BaseModel):
	id: int
	name: str
	description: str | None = None
	price: Decimal
	stock: int
	image_url: str | None = None
	created_at: datetime

	model_config = {
		"from_attributes": True
	}
