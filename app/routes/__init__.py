from flask import Flask


def init_app(app: Flask):

    from .categories_route import db as db_categories

    app.register_blueprint(db_categories)

    from .tasks_route import db as db_tasks

    app.register_blueprint(db_tasks)
