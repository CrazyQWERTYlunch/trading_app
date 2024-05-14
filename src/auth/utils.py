"""
Module defining utilities for user-related operations in the authentication system.

Functions:
    get_user_db: Asynchronous generator function to get the user database.
"""
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from src.database import get_async_session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    """
    Asynchronous generator function to get the user database.

    Args:
        session (AsyncSession, optional): The async database session.

    Yields:
        SQLAlchemyUserDatabase: The user database.
    """
    yield SQLAlchemyUserDatabase(session, User)