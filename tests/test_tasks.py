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
async def test_create_task(client: AsyncClient, test_user_data, test_task_data):
    """Test creating a task"""
    token = await get_auth_token(client, test_user_data)
    headers = {"Authorization": f"Bearer {token}"}

    response = await client.post("/api/tasks/", json=test_task_data, headers=headers)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == test_task_data["title"]
    assert data["description"] == test_task_data["description"]
    assert data["priority"] == test_task_data["priority"]
    assert data["is_completed"] is False


@pytest.mark.asyncio
async def test_get_tasks(client: AsyncClient, test_user_data, test_task_data):
    """Test getting all tasks"""
    token = await get_auth_token(client, test_user_data)
    headers = {"Authorization": f"Bearer {token}"}

    # Create a task
    await client.post("/api/tasks/", json=test_task_data, headers=headers)

    # Get all tasks
    response = await client.get("/api/tasks/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == test_task_data["title"]


@pytest.mark.asyncio
async def test_get_task_by_id(client: AsyncClient, test_user_data, test_task_data):
    """Test getting a task by ID"""
    token = await get_auth_token(client, test_user_data)
    headers = {"Authorization": f"Bearer {token}"}

    # Create a task
    create_response = await client.post("/api/tasks/", json=test_task_data, headers=headers)
    task_id = create_response.json()["id"]

    # Get task by ID
    response = await client.get(f"/api/tasks/{task_id}", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == test_task_data["title"]


@pytest.mark.asyncio
async def test_update_task(client: AsyncClient, test_user_data, test_task_data):
    """Test updating a task"""
    token = await get_auth_token(client, test_user_data)
    headers = {"Authorization": f"Bearer {token}"}

    # Create a task
    create_response = await client.post("/api/tasks/", json=test_task_data, headers=headers)
    task_id = create_response.json()["id"]

    # Update task
    update_data = {"title": "Updated Task", "is_completed": True}
    response = await client.put(f"/api/tasks/{task_id}", json=update_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Task"
    assert data["is_completed"] is True


@pytest.mark.asyncio
async def test_delete_task(client: AsyncClient, test_user_data, test_task_data):
    """Test deleting a task"""
    token = await get_auth_token(client, test_user_data)
    headers = {"Authorization": f"Bearer {token}"}

    # Create a task
    create_response = await client.post("/api/tasks/", json=test_task_data, headers=headers)
    task_id = create_response.json()["id"]

    # Delete task
    response = await client.delete(f"/api/tasks/{task_id}", headers=headers)
    assert response.status_code == 204

    # Verify task is deleted
    get_response = await client.get(f"/api/tasks/{task_id}", headers=headers)
    assert get_response.status_code == 404


@pytest.mark.asyncio
async def test_create_task_without_auth(client: AsyncClient, test_task_data):
    """Test creating a task without authentication"""
    response = await client.post("/api/tasks/", json=test_task_data)
    assert response.status_code == 401
