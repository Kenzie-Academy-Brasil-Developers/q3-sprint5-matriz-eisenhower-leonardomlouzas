from dataclasses import dataclass

import sqlalchemy
from app.configs.database import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


@dataclass
class TasksCategories(db.Model):
    id: int
    categories_id: int
    tasks_id: int

    __tablename__ = "tasks_categories"

    id = Column(Integer, primary_key=True)
    categories_id = Column(Integer, ForeignKey("categories.id"))
    tasks_id = Column(Integer, ForeignKey("tasks.id"))

    category = relationship("Category", back_populates="task_category", uselist=False)
    task = relationship("Task", back_populates="task_category", uselist=False)
