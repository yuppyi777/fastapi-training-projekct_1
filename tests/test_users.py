import pytest
from httpx import AsyncClient


async def get_auth_token(client: AsyncClient, user_data: dict) -> str:
    """Helper function to get authentication token"""
    # Register user
    await client.post("/api/auth/register", json=user_data)

    # Login
    response = await client.post(
        "/api/auth/login",
        data={"username": user_data["email"], "password": user_data["password"]},
    )
    return response.json()["access_token"]


@pytest.mark.asyncio
async def test_get_current_user(client: AsyncClient, test_user_data):
    """Test getting current user information"""
    token = await get_auth_token(client, test_user_data)
    headers = {"Authorization": f"Bearer {token}"}

    response = await client.get("/api/users/me", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == test_user_data["email"]
    assert data["username"] == test_user_data["username"]


@pytest.mark.asyncio
async def test_update_current_user(client: AsyncClient, test_user_data):
    """Test updating current user information"""
    token = await get_auth_token(client, test_user_data)
    headers = {"Authorization": f"Bearer {token}"}

    update_data = {"username": "updateduser"}
    response = await client.put("/api/users/me", json=update_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "updateduser"


@pytest.mark.asyncio
async def test_get_current_user_without_auth(client: AsyncClient):
    """Test getting current user without authentication"""
    response = await client.get("/api/users/me")
    assert response.status_code == 401
