from flask import Blueprint
from app.controllers.categories_controller import (
    retrieve_categories,
    create_category,
    fix_category,
    remove_category,
)


db = Blueprint("category", __name__)

db.get("/")(retrieve_categories)
db.post("/categories")(create_category)
db.patch("/categories/<category_id>")(fix_category)
db.delete("/categories/<category_id>")(remove_category)
