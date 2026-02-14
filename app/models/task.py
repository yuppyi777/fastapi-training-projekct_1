from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class Task(Base):
    """Task model"""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    is_completed = Column(Boolean, default=False)
    priority = Column(Integer, default=1)  # 1: Low, 2: Medium, 3: High
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # BUG: Relationship is commented out - students need to uncomment and fix
    user = relationship("User", back_populates="tasks")
