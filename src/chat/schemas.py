"""
Module defining Pydantic models for chat messages.

Attributes:
    MessagesModel: Pydantic model representing chat messages.

"""
from pydantic import BaseModel


class MessagesModel(BaseModel):
    """
    Pydantic model representing chat messages.

    Attributes:
        id (int): The unique identifier of the message.
        message (str): The content of the message.
    """
    id: int
    message: str

    class ConfigDict:
        from_atribures = True