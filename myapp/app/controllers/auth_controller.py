from fastapi import Request, Form, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from ..deps.db import get_db
from ..services.user_service import register as register_user, authenticate as authenticate_user
from ..schemas.user import UserCreate, UserLogin
from ..exceptions.domain import UserAlreadyExistsError, InvalidCredentialsError
from ..templates_config import templates


def register_page(request: Request):
    """Render the registration page."""
    if request.session.get("user_id"):
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse(request, "auth/register.html", {})


def register(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    """Handle user registration."""
    try:
        user_data = UserCreate(username=username, email=email, password=password)
        register_user(db, user_data)
        return RedirectResponse(url="/login", status_code=303)
    except UserAlreadyExistsError:
        return templates.TemplateResponse(
            request,
            "auth/register.html",
            {"error": "User with this email already exists"},
            status_code=400
        )


def login_page(request: Request):
    """Render the login page."""
    if request.session.get("user_id"):
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse(request, "auth/login.html", {})


def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    """Handle user login."""
    try:
        login_data = UserLogin(email=email, password=password)
        result = authenticate_user(db, login_data)
        user = result["user"]
        request.session["user_id"] = user.id
        return RedirectResponse(url="/", status_code=303)
    except InvalidCredentialsError:
        return templates.TemplateResponse(
            request,
            "auth/login.html",
            {"error": "Invalid email or password"},
            status_code=401
        )


def logout(request: Request):
    """Handle user logout."""
    request.session.clear()
    return RedirectResponse(url="/", status_code=303)