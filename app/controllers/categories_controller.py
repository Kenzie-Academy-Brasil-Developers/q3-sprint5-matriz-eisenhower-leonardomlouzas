from http import HTTPStatus
from flask import jsonify, request, session
from app.models.categories_model import Category
from app.models.tasks_categories_model import TasksCategories
from sqlalchemy.orm import Session
from app.configs.database import db
from sqlalchemy.exc import IntegrityError


def retrieve_categories():

    session: Session = db.session()

    tasks_categories = session.query(TasksCategories).all()
    categories = session.query(Category).all()

    categories = [
        {"id": category.id, "name": category.name, "description": category.description}
        for category in categories
    ]

    categories_id = [category["id"] for category in categories]

    for index, id in enumerate(categories_id):
        tasks = [
            {
                "id": task_category.task.id,
                "name": task_category.task.name,
                "description": task_category.task.description,
                "duration": task_category.task.duration,
                "classification": task_category.task.classification.type,
            }
            for task_category in tasks_categories
            if id == task_category.categories_id
        ]

        categories[index]["tasks"] = tasks

    return jsonify(categories), HTTPStatus.OK


def create_category():
    data = request.get_json()

    for key, value in data.items():
        data[key] = value.lower()

    try:
        category = Category(**data)

        session: Session = db.session()

        session.add(category)
        session.commit()

        return jsonify(category), HTTPStatus.CREATED

    except IntegrityError:
        return {"msg": "category already exists!"}, HTTPStatus.CONFLICT


def fix_category(category_id: int):
    data = request.get_json()

    for key, value in data.items():
        data[key] = value.lower()

    try:

        session: Session = db.session()

        category = session.query(Category).get(category_id)

        if not category:
            return {"msg": "category not found!"}, HTTPStatus.NOT_FOUND

        for key, value in data.items():
            setattr(category, key, value)

        session.add(category)
        session.commit()

        return jsonify(category), HTTPStatus.OK

    except IntegrityError:
        return {"msg": "category already exists!"}, HTTPStatus.CONFLICT


def remove_category(category_id: int):

    session: Session = db.session()

    category = session.query(Category).get(category_id)

    if not category:
        return {"msg": "category not found!"}, HTTPStatus.NOT_FOUND

    session.delete(category)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
