"""
Module defining the basic configuration for user authentication in the application.

Attributes:
    cookie_transport: Cookie transport configuration for authentication.
    auth_backend: Authentication backend configuration for JWT.
    fastapi_users: FastAPI Users instance for user management.
    current_user: Function to get the current authenticated user.

Functions:
    get_jwt_strategy: Function to get the JWT strategy for authentication.
"""
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, AuthenticationBackend, JWTStrategy

from .manager import get_user_manager
from .models import User
from src.config import SECRET_AUTH

cookie_transport = CookieTransport(cookie_name="bonds", cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    """Function to get the JWT strategy for authentication."""
    return JWTStrategy(secret=SECRET_AUTH, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()