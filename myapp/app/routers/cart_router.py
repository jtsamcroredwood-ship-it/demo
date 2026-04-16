from fastapi import APIRouter, Depends
from app.controllers.cart_controller import CartController

router = APIRouter(prefix="/cart", tags=["Cart"])

router.add_api_route("/", CartController.show_cart, methods=["GET"])
router.add_api_route("/add", CartController.add_to_cart, methods=["POST"])
router.add_api_route("/remove/{product_id}", CartController.remove_from_cart, methods=["POST"])
router.add_api_route("/update", CartController.update_cart_qty, methods=["POST"])
