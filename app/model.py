from tkinter import S
from turtle import title
from app import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f'{self.title}'

    def save_task(self):
        db.session.add(self)
        db.session.commit()
    
    def update_task(self, title):
        self.title = title

    def delete_task(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_task(cls, id):
        task = cls.query.filter_by(id=id).first()
        if task:
            return task
        return None
        
    def json(self):
        return {
            'id': self.id,
            'title': self.title
        }