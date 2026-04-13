from fastapi import APIRouter, Request
from app.controllers import product_controller

router = APIRouter()

@router.get("/", response_class=None)
async def list_products(request: Request):
	return await product_controller.list_products(request)

@router.get("/products/{product_id}", response_class=None)
async def product_detail(request: Request, product_id: int):
	return await product_controller.product_detail(request, product_id)
