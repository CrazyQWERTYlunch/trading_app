"""
Pydantic schemas for operations in the trading application.

This module defines Pydantic schemas for representing operations related to trading in the
trading application. It includes schemas for creating new operations.

Attributes:
    OperationCreate (BaseModel): Pydantic model for creating a new operation.
    
"""
from pydantic import BaseModel


class OperationCreate(BaseModel):
    """
    Pydantic schema for creating a new operation.

    Attributes:
        id (int): The ID of the operation.
        quantity (str): The quantity of the operation.
        figi (str): The FIGI (Financial Instrument Global Identifier) of the operation.
        instrument_type (str): The type of financial instrument associated with the operation.
        type (str): The type of operation (e.g., buy, sell, etc.).
        
    """
    id: int
    quantity: str
    figi: str
    instrument_type: str
    type: str