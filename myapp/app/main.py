from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.sessions import SessionMiddleware
from .config import settings
from .routers.auth_router import router as auth_router
from .routers.product_router import router as product_router
from .routers.cart_router import router as cart_router
from .routers.order_router import router as order_router
from .middleware.error_handler import DomainExceptionHandlerMiddleware
from .templates_config import templates

from fastapi.exception_handlers import http_exception_handler

app = FastAPI(title="E-commerce Lite", debug=settings.DEBUG)

@app.exception_handler(StarletteHTTPException)
async def auth_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 401:
        return RedirectResponse(url="/login", status_code=303)
    return await http_exception_handler(request, exc)

app.add_middleware(DomainExceptionHandlerMiddleware)
app.add_middleware(SessionMiddleware, secret_key=settings.SESSION_SECRET)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(auth_router)
app.include_router(product_router)
app.include_router(cart_router)
app.include_router(order_router)

@app.get("/health")
def health():
    return {"status": "ok"}