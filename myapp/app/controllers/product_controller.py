# Product controller for product views
from fastapi import Request, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.product_service import ProductService
from app.templates_config import templates

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

async def list_products(request: Request):
	db = next(get_db())
	service = ProductService(db)
	products = service.get_all_products()
	return templates.TemplateResponse("index.html", {"request": request, "products": products})

async def product_detail(request: Request, product_id: int):
	db = next(get_db())
	service = ProductService(db)
	product = service.get_product_detail(product_id)
	if not product:
		raise HTTPException(status_code=404, detail="Product not found")
	return templates.TemplateResponse("product_detail.html", {"request": request, "product": product})
