from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    """Base task schema"""

    title: str = Field(..., max_length=200)
    description: Optional[str] = None
    priority: int = Field(default=1, ge=1, le=3)


class TaskCreate(TaskBase):
    """Task creation schema"""

    pass


class TaskUpdate(BaseModel):
    """Task update schema"""

    title: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    priority: Optional[int] = Field(None, ge=1, le=3)


class TaskResponse(TaskBase):
    """Task response schema"""

    id: int
    is_completed: bool
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
