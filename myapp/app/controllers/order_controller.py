from fastapi import Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from app.deps.db import get_db
from app.deps.auth import get_current_user
from app.models.user import User
from app.services.order_service import OrderService
from app.repositories.order_repo import OrderRepository
from app.templates_config import templates

class OrderController:
    @staticmethod
    def checkout_post(
        request: Request, 
        user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
    ):
        order_service = OrderService()
        order_service.checkout(request, user, db)
        return RedirectResponse(url="/orders", status_code=303)

    @staticmethod
    def order_history(
        request: Request, 
        user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
    ):
        order_repo = OrderRepository(db)
        orders = order_repo.get_orders_by_user(user.id)
        return templates.TemplateResponse(
            request,
            "orders.html", 
            {"orders": orders, "user": user}
        )
