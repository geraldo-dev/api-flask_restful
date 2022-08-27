from flask_restful import Resource, reqparse
from app.model import Task

class TaskResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'title', type=str, required=True, help='this field cannot be left blank')
    
    def get(self):
        tasks = Task.query.all()
        data = []
        for task in tasks:
            data.append(task.json())
        return {'tasks': data }, 200

    def post(self):
        data = TaskResource.parser.parse_args()
        new_task = Task(**data)
        try:
            new_task.save_task()
            return { 'message': 'task has been created successfully.' }, 201
        except:
            return {'message': 'an error accurred creating the task.'}, 500

class TaskDetailResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'title', type=str, required=True, help='this field cannot be left blank')
    
    def get(self, id):
        task = Task.find_by_task(id)
        if task:
            return {'task': task.json()}, 200
        return {'message':'task not found'}, 404

    def put(self, id):
        data = TaskDetailResource.parser.parse_args()
        find_task  = Task.find_by_task(id)
        if find_task:
            try:
                find_task.update_task(**data)
                find_task.save_task()
                return find_task.json(), 200
            except:
                return {'message': 'an error occurred update the task'}, 500
        return {'message': 'task not fond'}, 404
    
    def delete(self, id):
        find_task  = Task.find_by_task(id)
        if find_task:
            try:
                find_task.delete_task()
                return {'message': 'deleted task'}, 200
            except:
                return {'message': 'an error occurred delete the task'}, 500
        return {'message': 'task not fond'}, 404