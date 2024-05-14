"""
This module defines SQLAlchemy models for authentication-related data, such as users and roles.
"""
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import ForeignKey, Integer, Column, JSON, String, TIMESTAMP, Table, Boolean, func

from src.database import Base, metadata


role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
    extend_existing=True
)


class User(SQLAlchemyBaseUserTable[int], Base):
    """
    SQLAlchemy model representing a user in the authentication system.

    Attributes:
        __tablename__ (str): The name of the database table for users.
        __table_args__ (dict): Additional arguments for the database table.
        id (Column): The primary key for the user table.
        email (Column): The email address of the user.
        username (Column): The username of the user.
        register_at (Column): The timestamp of user registration.
        role_id (Column): The foreign key reference to the role table.
        hashed_password (Column): The hashed password of the user.
        is_active (Column): Indicates whether the user account is active.
        is_superuser (Column): Indicates whether the user is a superuser.
        is_verified (Column): Indicates whether the user account is verified.
    """
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    register_at = Column(TIMESTAMP, default=func.now())
    role_id = Column(Integer, ForeignKey(role.c.id))
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
