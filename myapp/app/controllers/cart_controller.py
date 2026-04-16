from fastapi import Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from app.deps.db import get_db
from app.services.cart_service import CartService
from app.templates_config import templates

class CartController:
    @staticmethod
    def show_cart(request: Request, db: Session = Depends(get_db)):
        cart_service = CartService()
        cart_summary = cart_service.get_summary(request, db)
        error = request.query_params.get("error")
        return templates.TemplateResponse(
            request,
            "cart.html", 
            {"cart_summary": cart_summary, "error": error}
        )

    @staticmethod
    def add_to_cart(
        request: Request, 
        product_id: int = Form(...), 
        quantity: int = Form(1), 
        db: Session = Depends(get_db)
    ):
        if not request.session.get("user_id"):
            return RedirectResponse(url="/login", status_code=303)
            
        cart_service = CartService()
        cart_service.add(request, product_id, quantity, db)
        return RedirectResponse(url="/cart", status_code=303)

    @staticmethod
    def remove_from_cart(
        request: Request, 
        product_id: int, 
        db: Session = Depends(get_db)
    ):
        cart_service = CartService()
        cart_service.remove(request, product_id)
        return RedirectResponse(url="/cart", status_code=303)

    @staticmethod
    def update_cart_qty(
        request: Request,
        product_id: int = Form(...),
        quantity: int = Form(...),
        db: Session = Depends(get_db)
    ):
        cart_service = CartService()
        cart_service.update_qty(request, product_id, quantity, db)
        return RedirectResponse(url="/cart", status_code=303)
