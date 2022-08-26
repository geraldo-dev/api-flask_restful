from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

#config database
app.config.from_object('config')

db = SQLAlchemy(app)
Migrate(app, db)

#models
from app.model import Task

#controllers
from app.controller import TaskResource, TaskDetailResource

#routes
api.add_resource(TaskResource, '/')
api.add_resource(TaskDetailResource, '/<int:id>')
