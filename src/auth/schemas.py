"""
Module defining schemas for user-related data in the authentication system.

Classes:
    UserRead: Schema representing user data for reading.
    UserCreate: Schema representing user data for creation.
"""
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    """
    Schema representing user data for reading.

    Attributes:
        id (int): The user's unique identifier.
        username (str): The user's username.
        email (str): The user's email address.
        role_id (int): The identifier of the user's role.
        is_active (bool, optional): Flag indicating whether the user account is active.
        is_superuser (bool, optional): Flag indicating whether the user is a superuser.
        is_verified (bool, optional): Flag indicating whether the user's email is verified.
    """
    id: int
    username: str
    email: str
    role_id: int
    is_active: bool | None = True
    is_superuser: bool | None = False
    is_verified: bool | None = False

    class ConfigDict:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    """
    Schema representing user data for creation.

    Attributes:
        username (str): The user's username.
        email (str): The user's email address.
        password (str): The user's password.
        role_id (int): The identifier of the user's role.
        is_active (bool, optional): Flag indicating whether the user account is active.
        is_superuser (bool, optional): Flag indicating whether the user is a superuser.
        is_verified (bool, optional): Flag indicating whether the user's email is verified.
    """
    username: str
    email: str
    password: str
    role_id: int
    is_active: bool | None = True
    is_superuser: bool | None = False
    is_verified: bool | None = False


    