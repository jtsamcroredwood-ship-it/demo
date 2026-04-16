from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.controllers import product_controller

router = APIRouter()

@router.get("/products", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
async def list_products(request: Request):
	return await product_controller.list_products(request)

@router.get("/products/{product_id}", response_class=HTMLResponse)
async def product_detail(request: Request, product_id: int):
	return await product_controller.product_detail(request, product_id)
