from dataclasses import asdict, dataclass
from enum import unique
from app.configs.database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


@dataclass
class Category(db.Model):

    id: int
    name: str
    description: str

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String)

    task_category = relationship("TasksCategories", back_populates="category")

    def asdict(self):
        return asdict(self)
