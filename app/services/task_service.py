from typing import List, Optional

from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskStats


class TaskService:
    """Task service for business logic"""

    @staticmethod
    async def get_tasks_by_user(
        db: AsyncSession, user_id: int, skip: int = 0, limit: int = 100, priority: Optional[int] = None, search: Optional[str] = None
    ) -> List[Task]:
        """Get all tasks for a user"""
        query = select(Task).where(Task.user_id == user_id)
        if priority is not None:
            query = query.where(Task.priority == priority)
        if search is not None:
            pattern = f"%{search}%"
            query = query.where(or_(Task.title.ilike(pattern), Task.description.ilike(pattern)))
        result = await db.execute(query.offset(skip).limit(limit))
        return list(result.scalars().all())

    @staticmethod
    async def get_task_by_id(db: AsyncSession, task_id: int, user_id: int) -> Optional[Task]:
        """Get task by ID for specific user"""
        result = await db.execute(
            select(Task).where(Task.id == task_id, Task.user_id == user_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def create_task(db: AsyncSession, task_data: TaskCreate, user_id: int) -> Task:
        """Create new task"""
        db_task = Task(**task_data.model_dump(), user_id=user_id)
        db.add(db_task)
        await db.commit()
        await db.refresh(db_task)
        return db_task

    @staticmethod
    async def update_task(
        db: AsyncSession, task_id: int, task_data: TaskUpdate, user_id: int
    ) -> Optional[Task]:
        """Update task"""
        db_task = await TaskService.get_task_by_id(db, task_id, user_id)
        if not db_task:
            return None

        update_data = task_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_task, field, value)

        await db.commit()
        await db.refresh(db_task)
        return db_task

    @staticmethod
    async def delete_task(db: AsyncSession, task_id: int, user_id: int) -> bool:
        """Delete task"""
        db_task = await TaskService.get_task_by_id(db, task_id, user_id)
        if not db_task:
            return False

        await db.delete(db_task)
        await db.commit()
        return True

    @staticmethod
    async def get_completed_tasks_count(db: AsyncSession, user_id: int) -> int:
        """Get count of completed tasks for user"""
        # 以前は全タスクをカウントしていたバグを修正
        result = await db.execute(select(Task).where(Task.user_id == user_id, Task.is_completed == True))
        tasks = result.scalars().all()
        return len(tasks)

    @staticmethod
    async def get_tasks_count(db: AsyncSession, user_id: int) -> int:
        """Get total count of tasks for user"""
        result = await db.execute(select(Task).where(Task.user_id == user_id))
        tasks = result.scalars().all()
        return len(tasks)

    @staticmethod
    async def get_task_statistics(db: AsyncSession, user_id: int) -> TaskStats:
        """Get task statistics"""
        total = await TaskService.get_tasks_count(db, user_id)
        completed = await TaskService.get_completed_tasks_count(db, user_id)
        pending = total - completed
        return TaskStats(total=total, completed=completed, pending=pending)