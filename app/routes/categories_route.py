from flask import Blueprint
from app.controllers.categories_controller import (
    retrieve_categories,
    create_category,
    fix_category,
    remove_category,
)


db = Blueprint("category", __name__, url_prefix="/categories")

db.get("")(retrieve_categories)
db.post("")(create_category)
db.patch("<category_id>")(fix_category)
db.delete("<category_id>")(remove_category)
