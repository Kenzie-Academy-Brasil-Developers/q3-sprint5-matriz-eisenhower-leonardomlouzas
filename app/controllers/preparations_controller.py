from tkinter import E
from sqlalchemy.orm.session import Session
from app.configs.database import db
from app.models.eisenhower_model import Eisenhower


def eisenhower_populate_table():

    categories = ["Do It First", "Schedule It", "Delegate It", "Delete It"]

    session: Session = db.session
    eisenhower = session.query(Eisenhower).all()

    # verifies if the table is already populates
    if not eisenhower:

        for category in categories:
            eisenhower = Eisenhower(**{"type": category})
            session.add(eisenhower)
            session.commit()

    return
