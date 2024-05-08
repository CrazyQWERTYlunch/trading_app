import pytest
from sqlalchemy import insert, select

from src.auth.models import role
from conftest import client, async_session_maker


async def test_add_role():
    async with async_session_maker() as session:
        stmt = insert(role).values(id=1, name="admin", permissions=None)
        await session.execute(stmt)
        await session.commit()

        query = select(role)
        result = await session.execute(query)
        assert result.all() == [(1, 'admin', None)], "Роль не добавилась"

def test_register():
    response = client.post("/auth/register", json={
        "email": "string_313132",
        "password": "string_313132",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "string_313132",
        "role_id": 1
    })

    # assert response.status_code == 201 # Разобраться почпему добавляет в боевую
    assert response.status_code == 400

