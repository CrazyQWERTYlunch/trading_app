"""
Tests for operations functionality.

This module contains tests for adding specific operations and getting specific operations.

Attributes:
    ac (AsyncClient): Async HTTP client for making requests.
"""
from httpx import AsyncClient


async def test_add_specific_operations(ac: AsyncClient):
    """
    Test adding specific operations.

    This test checks if a specific operation is successfully added via the endpoint.

    Args:
        ac (AsyncClient): Async HTTP client for making requests.

    Returns:
        None
    """
    response = await ac.post("/operations", json={
        "id": 1,
        "quantity": "25.5",
        "figi": "figi_CODE",
        "instrument_type": "bond",
        "type": "Выплата купонов",
    })

    assert response.status_code == 200 


async def test_get_specific_operations(ac: AsyncClient):
    """
    Test getting specific operations.

    This test checks if specific operations are successfully retrieved via the endpoint.

    Args:
        ac (AsyncClient): Async HTTP client for making requests.

    Returns:
        None
    """
    response = await ac.get("/operations", params={
        "operation_type": "Выплата купонов",
    })

    assert response.status_code == 200 
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 1