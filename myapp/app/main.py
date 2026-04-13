from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from .config import settings
from .routers.auth_router import router as auth_router
from .routers.product_router import router as product_router
from .templates_config import templates

app = FastAPI(title="E-commerce Lite", debug=settings.DEBUG)

app.add_middleware(SessionMiddleware, secret_key=settings.SESSION_SECRET)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(auth_router)
app.include_router(product_router)

@app.get("/health")
def health():
    return {"status": "ok"}