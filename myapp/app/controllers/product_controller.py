# Product controller for product views
from fastapi import Request, HTTPException, Depends
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.product_service import ProductService
from app.templates_config import templates

async def list_products(request: Request):
    db = SessionLocal()
    try:
        service = ProductService(db)
        products = service.get_all_products()
        return templates.TemplateResponse(
            request,
            "index.html",
            {"products": products}
        )
    finally:
        db.close()

async def product_detail(request: Request, product_id: int):
    db = SessionLocal()
    try:
        service = ProductService(db)
        product = service.get_product_detail(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return templates.TemplateResponse(
            request,
            "product_detail.html",
            {"product": product}
        )
    finally:
        db.close()
