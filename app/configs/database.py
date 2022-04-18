from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

db = SQLAlchemy()


def init_app(app: Flask):

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.db = db

    from app.models.tasks_model import Task
    from app.models.categories_model import Category
    from app.models.tasks_categories_model import TasksCategories
    from app.models.eisenhower_model import Eisenhower
