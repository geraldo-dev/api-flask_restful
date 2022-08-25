from flask_restful import Resource, reqparse
from app.model import Task

class TaskResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'title', type=str, required=True, help='this field cannot be left blank')
    
    def get(self):
        return {'msg':'hello'}