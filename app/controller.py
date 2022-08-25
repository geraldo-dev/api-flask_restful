from flask_restful import Resource, reqparse
from app.model import Task

class TaskResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'title', type=str, required=True, help='this field cannot be left blank')
    
    def get(self):
        return {'msg':'get'}

    def post(self):
        return {'msg': 'create'}

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