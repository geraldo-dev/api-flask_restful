from flask_restful import Resource, reqparse
from app.model import Task

class TaskResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'title', type=str, required=True, help='this field cannot be left blank')
    
    def get(self):
        return {'msg':'get'}

    def post(self):
        data = TaskResource.parser.parse_args()
        new_task = Task(**data)
        try:
            new_task.save_task()
            return { 'message': 'task has been created successfully.' }
        except:
            return {'message': 'an error accurred creating the task.'}

class TaskDetailResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'title', type=str, required=True, help='this field cannot be left blank')
    
    def get(self, id):
        return {'msg':'get-id'}

    def put(self, id):
        return {'msg': 'put'}
    
    def delete(self, id):
        return {'msg': 'delete'}