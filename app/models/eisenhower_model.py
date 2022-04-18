from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


@dataclass
class Eisenhower(db.Model):
    id: int
    type: str

    __tablename__ = "eisenhower"

    id = Column(Integer, primary_key=True)
    type = Column(String)

    task = relationship("Task", back_populates="classification", uselist=True)
