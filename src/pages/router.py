"""
API routes for rendering HTML pages.

This module defines API routes for rendering HTML pages using Jinja2 templates.
It includes routes for rendering the base page, search page, and chat page.

Attributes:
    router (APIRouter): FastAPI router for defining API endpoints related to rendering HTML pages.
    templates (Jinja2Templates): Jinja2 templates loader for rendering HTML templates.
    
"""
from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from src.operations.router import get_specific_operations

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/templates")

@router.get("/base")
def get_base_page(request: Request):
    """
    Endpoint to render the base page.

    Renders the base page using the base.html template.

    Args:
        request (Request): The incoming request.

    Returns:
        TemplateResponse: HTML template response for the base page.

    """
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/search/{operation_type}")
def get_search_page(request: Request, operations=Depends(get_specific_operations)):
    """
    Endpoint to render the search page.

    Renders the search page using the search.html template.

    Args:
        request (Request): The incoming request.
        operations (dict): Data retrieved from the specific operations endpoint.

    Returns:
        TemplateResponse: HTML template response for the search page.

    """
    return templates.TemplateResponse("search.html", {"request": request, "operations": operations["data"]})

@router.get("/chat")
def get_chat_page(request: Request):
    """
    Endpoint to render the chat page.

    Renders the chat page using the chat.html template.

    Args:
        request (Request): The incoming request.

    Returns:
        TemplateResponse: HTML template response for the chat page.

    """
    return templates.TemplateResponse("chat.html", {"request": request})