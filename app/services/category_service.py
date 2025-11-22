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
        """
        Get all categories for a user

        Args:
            db: Database session
            user_id: User ID
            skip: Number of records to skip
            limit: Maximum number of records to return

        Returns:
            List of Category objects
        """
        # TODO: Implement this method
        # Hint: Use select(Category).where(...).offset(...).limit(...)
        pass

    @staticmethod
    async def get_category_by_id(
        db: AsyncSession, category_id: int, user_id: int
    ) -> Optional[Category]:
        """
        Get category by ID for specific user

        Args:
            db: Database session
            category_id: Category ID
            user_id: User ID

        Returns:
            Category object or None
        """
        # TODO: Implement this method
        pass

    @staticmethod
    async def create_category(
        db: AsyncSession, category_data: CategoryCreate, user_id: int
    ) -> Category:
        """
        Create new category

        Args:
            db: Database session
            category_data: Category creation data
            user_id: User ID

        Returns:
            Created Category object
        """
        # TODO: Implement this method
        # Hint: Create Category instance, add to db, commit, refresh
        pass

    @staticmethod
    async def update_category(
        db: AsyncSession, category_id: int, category_data: CategoryUpdate, user_id: int
    ) -> Optional[Category]:
        """
        Update category

        Args:
            db: Database session
            category_id: Category ID
            category_data: Category update data
            user_id: User ID

        Returns:
            Updated Category object or None
        """
        # TODO: Implement this method
        pass

    @staticmethod
    async def delete_category(db: AsyncSession, category_id: int, user_id: int) -> bool:
        """
        Delete category

        Args:
            db: Database session
            category_id: Category ID
            user_id: User ID

        Returns:
            True if deleted, False if not found
        """
        # TODO: Implement this method
        pass
