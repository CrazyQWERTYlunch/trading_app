"""
Fixture setup for testing.

This module provides fixture setup for testing, including database setup and client setup.

Attributes:
    DATABASE_URL_TEST (str): Database URL for testing.
    engine_test (create_async_engine): Async database engine for testing.
    async_session_maker (sessionmaker): Async session maker for testing.
"""
import asyncio
from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from src.database import get_async_session
from src import metadata
from src.config import (DB_HOST_TEST, DB_NAME_TEST, DB_PASS_TEST, DB_PORT_TEST,
                        DB_USER_TEST)
from src.main import app

# DATABASE
DATABASE_URL_TEST = f"postgresql+asyncpg://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"

engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)
metadata.bind = engine_test

async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Override the get_async_session dependency for testing.

    Yields:
        AsyncSession: The async database session for testing.
    """
    async with async_session_maker() as session:
        yield session

app.dependency_overrides[get_async_session] = override_get_async_session

@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    """
    Prepare the database for testing.

    This fixture sets up the database for testing, including creating and dropping all tables.

    Yields:
        None
    """
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.drop_all)

# SETUP
@pytest.fixture(scope='session')
def event_loop(request):
    """
    Create an event loop for each test session.

    This fixture creates an instance of the default event loop for each test session.

    Args:
        request: The test request.

    Yields:
        asyncio.AbstractEventLoop: The event loop for testing.
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

client = TestClient(app)

@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    """
    Async client setup for testing.

    This fixture sets up an async client for testing with the test app.

    Yields:
        AsyncClient: The async client for testing.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac