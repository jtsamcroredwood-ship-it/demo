from fastapi import APIRouter
from app.controllers.order_controller import OrderController

router = APIRouter(tags=["Orders"])

router.add_api_route("/checkout", OrderController.checkout_post, methods=["POST"])
router.add_api_route("/orders", OrderController.order_history, methods=["GET"])
