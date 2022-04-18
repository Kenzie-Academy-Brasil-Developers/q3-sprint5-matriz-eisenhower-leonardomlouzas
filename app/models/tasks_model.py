from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


@dataclass
class Task(db.Model):
    id: int
    name: str
    description: str
    duration: int
    importance: int
    urgency: int

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)
    eisenhower_id = Column(Integer, ForeignKey("eisenhower.id"))

    classification = relationship("Eisenhower", back_populates="task")
    task_category = relationship("TasksCategories", back_populates="task", uselist=True)
