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
    # token = await get_auth_token(client, test_user_data)
    # headers = {"Authorization": f"Bearer {token}"}
    # ... implement the rest
    pass


@pytest.mark.asyncio
async def test_get_categories(client: AsyncClient, test_user_data, test_category_data):
    """
    Test getting all categories

    TODO: Implement this test
    Steps:
    1. Get auth token
    2. Create a category
    3. GET /api/categories/
    4. Assert status_code == 200
    5. Assert response is a list with at least 1 item
    """
    pass


@pytest.mark.asyncio
async def test_get_category_by_id(client: AsyncClient, test_user_data, test_category_data):
    """
    Test getting a category by ID

    TODO: Implement this test
    """
    pass


@pytest.mark.asyncio
async def test_update_category(client: AsyncClient, test_user_data, test_category_data):
    """
    Test updating a category

    TODO: Implement this test
    """
    pass


@pytest.mark.asyncio
async def test_delete_category(client: AsyncClient, test_user_data, test_category_data):
    """
    Test deleting a category

    TODO: Implement this test
    """
    pass


@pytest.mark.asyncio
async def test_create_category_without_auth(client: AsyncClient, test_category_data):
    """
    Test creating a category without authentication

    TODO: Implement this test
    Hint: Should return 401 status code
    """
    pass


# BONUS TODO: 追加のテストケース
# - test_create_category_with_invalid_color - 無効な色コードでの作成
# - test_get_category_not_found - 存在しないカテゴリの取得
# - test_update_category_not_owned - 他人のカテゴリの更新
