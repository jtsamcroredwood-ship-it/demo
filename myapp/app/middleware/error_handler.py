from fastapi import Request, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.base import BaseHTTPMiddleware
from app.exceptions.domain import DomainError, InsufficientStockError, ProductNotFoundError, EmptyCartError
import urllib.parse

class DomainExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except EmptyCartError as e:
            # Redirect to cart with an error message
            return RedirectResponse(url=f"/cart?error={urllib.parse.quote(str(e))}", status_code=303)
        except InsufficientStockError as e:
            # Redirect to cart with an error message
            return RedirectResponse(url=f"/cart?error={urllib.parse.quote(str(e))}", status_code=303)
        except ProductNotFoundError as e:
            # Redirect to products with error
            return RedirectResponse(url=f"/products?error={urllib.parse.quote(str(e))}", status_code=303)
        except DomainError as e:
            if "cart" in request.url.path or "checkout" in request.url.path:
                return RedirectResponse(url=f"/cart?error={urllib.parse.quote(str(e))}", status_code=303)
            raise HTTPException(status_code=400, detail=str(e))
