"""
SQLAlchemy models for operations in the trading application.

This module defines SQLAlchemy models for representing operations related to trading in the
trading application. It includes a model for operations such as buying, selling, or other
types of transactions.

Attributes:
    operation (Table): SQLAlchemy Table representing operations in the database.
"""
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, func
from src.database import metadata


operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantity", String),
    Column("figi", String),
    Column("instrument_type", String, nullable=True),
    Column("date", TIMESTAMP, default=func.now()),
    Column("type", String),
    extend_existing=True
)