"""
Category Service

TODO: 受講生の課題 - このサービスを完成させてください

必要な実装:
1. get_categories_by_user: ユーザーのカテゴリ一覧を取得
2. get_category_by_id: IDでカテゴリを取得
3. create_category: 新しいカテゴリを作成
4. update_category: カテゴリを更新
5. delete_category: カテゴリを削除

参考: app/services/task_service.py を参考にして実装してください
"""

from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate


class CategoryService:
    """Category service for business logic"""

    # TODO: 以下のメソッドを実装してください

    @staticmethod
    async def get_categories_by_user(
        db: AsyncSession, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Category]:
        """Get all categories for a user"""
        query = select(Category).where(Category.user_id == user_id)
        result = await db.execute(query.offset(skip).limit(limit))
        return list(result.scalars().all())

    @staticmethod
    async def get_category_by_id(
        db: AsyncSession, category_id: int, user_id: int
    ) -> Optional[Category]:
        """Get category by ID for specific user"""
        result = await db.execute(
            select(Category).where(Category.id == category_id, Category.user_id == user_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def create_category(
        db: AsyncSession, category_data: CategoryCreate, user_id: int
    ) -> Category:
        """Create new category"""
        db_category = Category(**category_data.model_dump(), user_id=user_id)
        db.add(db_category)
        await db.commit()
        await db.refresh(db_category)
        return db_category

    @staticmethod
    async def update_category(
        db: AsyncSession, category_id: int, category_data: CategoryUpdate, user_id: int
    ) -> Optional[Category]:
        """Update category"""
        db_category = await CategoryService.get_category_by_id(db, category_id, user_id)
        if not db_category:
            return None

        update_data = category_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_category, field, value)

        await db.commit()
        await db.refresh(db_category)
        return db_category

    @staticmethod
    async def delete_category(db: AsyncSession, category_id: int, user_id: int) -> bool:
        """Delete category"""
        db_category = await CategoryService.get_category_by_id(db, category_id, user_id)
        if not db_category:
            return False

        await db.delete(db_category)
        await db.commit()
        return True
