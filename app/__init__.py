import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder=os.path.join('..', 'view', 'templates'))
    app.config.from_object('config.Config')

    db.init_app(app)

    from controllers.user_controller import UserController
    from controllers.task_controller import TaskController
    
    app.add_url_rule('/', view_func=UserController.index, endpoint='index')
    app.add_url_rule('/contact', view_func=UserController.contact, methods=['GET', 'POST'], endpoint='contact')
    app.add_url_rule("/tasks", view_func=TaskController.list_tasks, endpoint="list_tasks")
    app.add_url_rule("/tasks/new", view_func=TaskController.create_task, methods=["GET", "POST"], endpoint="create_task")
    app.add_url_rule("/tasks/update/<int:task_id>", view_func=TaskController.update_task_status, methods=["POST"], endpoint="update_task_status")
    app.add_url_rule("/tasks/delete/<int:task_id>", view_func=TaskController.delete_task, methods=["POST"], endpoint="delete_task")

    return app