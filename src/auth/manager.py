"""
Module defining the user manager for user authentication and management.

Attributes:
    UserManager: Manager class for user authentication and management.

Functions:
    get_user_manager: Function to get the user manager instance.
"""
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models, schemas

from .models import User
from .utils import get_user_db

from src.config import SECRET_AUTH


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    """
    Manager class for user authentication and management.

    Attributes:
        reset_password_token_secret (str): Secret key for reset password token.
        verification_token_secret (str): Secret key for verification token.

    Methods:
        on_after_register: Method executed after user registration.
        create: Method to create a new user.

    Parameters:
        user_create (schemas.UC): The user creation schema.
        safe (bool, optional): A flag indicating if the user creation is safe.
        request (Optional[Request], optional): The request object.

    Returns:
        models.UP: The created user object.

    Raises:
        exceptions.UserAlreadyExists: If a user with the same email already exists.
    """
    reset_password_token_secret = SECRET_AUTH
    verification_token_secret = SECRET_AUTH

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        """Method executed after user registration."""
        print(f"User {user.id} has registered.")

    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        """Method to create a new user."""
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)
        user_dict["role_id"] = 1

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user


async def get_user_manager(user_db=Depends(get_user_db)):
    """Function to get the user manager instance.
        Parameters:
            user_db: Dependency for getting the user database.

        Returns:
            UserManager: The user manager instance.
    """
    yield UserManager(user_db)