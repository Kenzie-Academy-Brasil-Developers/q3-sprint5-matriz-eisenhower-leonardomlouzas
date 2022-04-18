from http import HTTPStatus
from flask import jsonify, request
from app.models.tasks_categories_model import TasksCategories
from app.models.tasks_model import Task
from app.models.categories_model import Category
from sqlalchemy.orm import Session
from app.configs.database import db
from sqlalchemy.exc import IntegrityError


def create_task():

    data = request.get_json()

    categories = data.pop("categories")

    # Verifies if 'importance' and 'urgency' are in sent data
    if "importance" not in data or "urgency" not in data:
        return {"msg": "Must provide 'importance and 'urgency' keys"}

    # Verifies and sets eisenhower level
    if data["importance"] == 1 and data["urgency"] == 1:
        data["eisenhower_id"] = 1

    elif data["importance"] == 1 and data["urgency"] == 2:
        data["eisenhower_id"] = 2

    elif data["importance"] == 2 and data["urgency"] == 1:
        data["eisenhower_id"] = 3

    elif data["importance"] == 2 and data["urgency"] == 2:
        data["eisenhower_id"] = 4

    else:

        return {
            "msg": {
                "valid_options": {"importance": [1, 2], "urgency": [1, 2]},
                "received_options": {
                    "importance": data["importance"],
                    "urgency": data["urgency"],
                },
            }
        }, HTTPStatus.BAD_REQUEST

    try:
        session: Session = db.session()

        task = Task(**data)

        session.add(task)
        session.commit()

    except IntegrityError:
        return {"msg": "task already exists!"}, HTTPStatus.CONFLICT

    for category in categories:
        existent_category = (
            session.query(Category).filter_by(name=category).one_or_none()
        )

        if not existent_category:
            new_category = Category(**{"name": category})
            session.add(new_category)
            session.commit()

            task_category = TasksCategories(
                **{"categories_id": new_category.id, "tasks_id": task.id}
            )
            session.add(task_category)
            session.commit()

        else:
            task_category = TasksCategories(
                **{"categories_id": existent_category.id, "tasks_id": task.id}
            )
            session.add(task_category)
            session.commit()

    task = {
        "id": task.id,
        "name": task.name,
        "description": task.description,
        "duration": task.duration,
        "classification": task.classification.type,
        "categories": list(task.task_category),
    }

    arr = []

    for category in task["categories"]:
        category = session.query(Category).get(category.categories_id)
        arr.append(category.name)

    task["categories"] = arr

    return task, HTTPStatus.CREATED


def fix_task(task_id: int):

    available_priorities = [1, 2]

    data = request.get_json()

    session: Session = db.session()

    task = session.query(Task).get(task_id)

    if not task:
        return {"msg": "task not found!"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        if key == "importance" or key == "urgency":
            if value not in available_priorities:
                return {
                    "msg": "'importance' and 'urgency' must be 1 or 2"
                }, HTTPStatus.BAD_REQUEST

        setattr(task, key, value)

    if task.importance == 1 and task.urgency == 1:
        task.eisenhower_id = 1
    elif task.importance == 1 and task.urgency == 2:
        task.eisenhower_id = 2
    elif task.importance == 2 and task.urgency == 1:
        task.eisenhower_id = 3
    elif task.importance == 2 and task.urgency == 2:
        task.eisenhower_id = 4
    else:
        print(f"{task.eisenhower_id=}")
        return jsonify("erro nos elifs")

    session.add(task)
    session.commit()

    task = {
        "id": task.id,
        "name": task.name,
        "description": task.description,
        "duration": task.duration,
        "classification": task.classification.type,
        "categories": list(task.task_category),
    }

    arr = []

    for category in task["categories"]:
        category = session.query(Category).get(category.categories_id)
        arr.append(category.name)

    task["categories"] = arr

    return jsonify(task), HTTPStatus.OK


def remove_task(task_id: int):

    session: Session = db.session()

    task = session.query(Task).get(task_id)

    if not task:
        return {"msg": "task not found!"}, HTTPStatus.NOT_FOUND

    session.delete(task)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
