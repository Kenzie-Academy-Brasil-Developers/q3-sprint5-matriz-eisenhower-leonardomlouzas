from flask import Blueprint
from app.controllers.tasks_controller import create_task, fix_task, remove_task
from app.controllers.preparations_controller import eisenhower_populate_table

db = Blueprint("tasks", __name__, url_prefix="/tasks")

db.before_app_first_request(eisenhower_populate_table)
db.post("")(create_task)
db.patch("<task_id>")(fix_task)
db.delete("<task_id>")(remove_task)
