"""
Category API Endpoints

TODO: 受講生の課題 - このAPIエンドポイントを完成させてください

必要な実装:
1. GET /api/categories/ - カテゴリ一覧取得
2. POST /api/categories/ - カテゴリ作成
3. GET /api/categories/{category_id} - カテゴリ詳細取得
4. PUT /api/categories/{category_id} - カテゴリ更新
5. DELETE /api/categories/{category_id} - カテゴリ削除

参考: app/api/tasks.py を参考にして実装してください
注意: 認証が必要です (get_current_active_user を使用)
"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_active_user
from app.core.database import get_db
from app.models.user import User
from app.schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate
from app.services.category_service import CategoryService

router = APIRouter(prefix="/categories", tags=["Categories"])


# TODO: 以下のエンドポイントを実装してください


@router.get("/", response_model=List[CategoryResponse])
async def get_categories(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    """Get all categories for current user"""
    categories = await CategoryService.get_categories_by_user(db, current_user.id, skip, limit)
    return categories


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(
    category_data: CategoryCreate,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    """Create new category"""
    category = await CategoryService.create_category(db, category_data, current_user.id)
    return category


@router.get("/{category_id}", response_model=CategoryResponse)
async def get_category(
    category_id: int,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    """Get category by ID"""
    category = await CategoryService.get_category_by_id(db, category_id, current_user.id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category


@router.put("/{category_id}", response_model=CategoryResponse)
async def update_category(
    category_id: int,
    category_data: CategoryUpdate,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    """Update category"""
    category = await CategoryService.update_category(db, category_id, category_data, current_user.id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category_id: int,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    """Delete category"""
    success = await CategoryService.delete_category(db, category_id, current_user.id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")


# BONUS TODO: カテゴリに紐づくタスク一覧を取得するエンドポイントを追加
# @router.get("/{category_id}/tasks", response_model=List[TaskResponse])
# async def get_category_tasks(...):
#     """Get all tasks in a category"""
#     pass
