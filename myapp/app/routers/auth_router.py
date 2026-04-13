from fastapi import APIRouter
from ..controllers.auth_controller import register_page, register, login_page, login, logout

router = APIRouter()

router.get("/register")(register_page)
router.post("/register")(register)
router.get("/login")(login_page)
router.post("/login")(login)
router.post("/logout")(logout)