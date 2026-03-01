"""
Category API Tests

TODO: 受講生の課題 - このテストを完成させてください

必要なテスト:
1. test_create_category - カテゴリ作成のテスト
2. test_get_categories - カテゴリ一覧取得のテスト
3. test_get_category_by_id - カテゴリ詳細取得のテスト
4. test_update_category - カテゴリ更新のテスト
5. test_delete_category - カテゴリ削除のテスト
6. test_create_category_without_auth - 認証なしでの作成失敗テスト

参考: tests/test_tasks.py を参考にして実装してください
"""

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


@pytest.fixture
def test_category_data():
    """Test category data"""
    return {
        "name": "Work",
        "description": "Work related tasks",
        "color": "#FF5733",
    }


# TODO: 以下のテストを実装してください


@pytest.mark.asyncio
async def test_create_category(client: AsyncClient, test_user_data, test_category_data):
    """
    Test creating a category

    TODO: Implement this test
    Steps:
    1. Get auth token
    2. POST /api/categories/ with test_category_data
    3. Assert status_code == 201
    4. Assert response contains correct data
    """
    token = await get_auth_token(client, test_user_data)
    headers = {"Authorization": f"Bearer {token}"}

    # Create a category
    response = await client.post("/api/categories/", json=test_category_data, headers=headers)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == test_category_data["name"]
    assert data["description"] == test_category_data["description"]
    assert data["color"] == test_category_data["color"]


@pytest.mark.asyncio
async def test_get_categories(client: AsyncClient, test_user_data, test_category_data):
    """Test getting all categories"""
    token = await get_auth_token(client, test_user_data)
    headers = {"Authorization": f"Bearer {token}"}

    # TODO: Create a category  
    await client.post("/api/categories/", json=test_category_data, headers=headers)

    # Get all categories
    response = await client.get("/api/categories/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == test_category_data["name"]


@pytest.mark.asyncio
async def test_get_category_by_id(client: AsyncClient, test_user_data, test_category_data):
    """Test getting a category by ID"""
    token = await get_auth_token(client, test_user_data)
    headers = {"Authorization": f"Bearer {token}"}

    # Create a category
    response = await client.post("/api/categories/", json=test_category_data, headers=headers)
    category_id = response.json()["id"]

    # Get category by ID
    response = await client.get(f"/api/categories/{category_id}", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == category_id
    assert data["name"] == test_category_data["name"]


@pytest.mark.asyncio
async def test_update_category(client: AsyncClient, test_user_data, test_category_data):
    """Test updating a category"""
    token = await get_auth_token(client, test_user_data)
    headers = {"Authorization": f"Bearer {token}"}

    # Create a category
    response = await client.post("/api/categories/", json=test_category_data, headers=headers)
    category_id = response.json()["id"]

    # Update category
    update_data = {"name": "Updated Category"}
    response = await client.put(f"/api/categories/{category_id}", json=update_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Category"


@pytest.mark.asyncio
async def test_delete_category(client: AsyncClient, test_user_data, test_category_data):
    """Test deleting a category"""
    token = await get_auth_token(client, test_user_data)
    headers = {"Authorization": f"Bearer {token}"}

    # Create a category
    response = await client.post("/api/categories/", json=test_category_data, headers=headers)
    category_id = response.json()["id"]

    # Delete category
    response = await client.delete(f"/api/categories/{category_id}", headers=headers)
    assert response.status_code == 204

    # Verify category is deleted
    response = await client.get(f"/api/categories/{category_id}", headers=headers)
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_create_category_without_auth(client: AsyncClient, test_category_data):
    """Test creating a category without authentication"""
    response = await client.post("/api/categories/", json=test_category_data)
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_get_category_not_found(client: AsyncClient, test_user_data, test_category_data):
    """Test getting a category that does not exist"""

    token = await get_auth_token(client, test_user_data)
    headers = {"Authorization": f"Bearer {token}"}

    # Create a category
    response = await client.post("/api/categories/", json=test_category_data, headers=headers)
    category_id = response.json()["id"]
    # 存在しないカテゴリID
    next_category_id = category_id + 1

    # Get category by ID
    response = await client.get(f"/api/categories/{next_category_id}", headers=headers)
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_update_category_not_found(client: AsyncClient, test_user_data, test_category_data):
    """Test updating a category that does not exist"""
    token = await get_auth_token(client, test_user_data)
    headers = {"Authorization": f"Bearer {token}"}

    # Create a category
    response = await client.post("/api/categories/", json=test_category_data, headers=headers)
    category_id = response.json()["id"]
    next_category_id = category_id + 1

    # Update category
    update_data = {"name": "Updated Category"}
    response = await client.put(f"/api/categories/{next_category_id}", json=update_data, headers=headers)
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_delete_category_not_found(client: AsyncClient, test_user_data, test_category_data):
    """Test deleting a category that does not exist"""
    token = await get_auth_token(client, test_user_data)
    headers = {"Authorization": f"Bearer {token}"}

    # Create a category
    response = await client.post("/api/categories/", json=test_category_data, headers=headers)
    category_id = response.json()["id"]
    # 存在しないカテゴリID
    next_category_id = category_id + 1

    # Delete category
    response = await client.delete(f"/api/categories/{next_category_id}", headers=headers)
    assert response.status_code == 404

# BONUS TODO: 追加のテストケース
# - test_create_category_with_invalid_color - 無効な色コードでの作成
# - test_get_category_not_found - 存在しないカテゴリの取得
# - test_update_category_not_owned - 他人のカテゴリの更新
