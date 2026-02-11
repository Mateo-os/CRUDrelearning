from flask import request, jsonify
from app.database import db
from app.models import Task


def register_routes(app):
   
    @app.route("/tasks",methods=["POST"])
    def create_task():
        data = request.get_json()
        task = Task(title=data["title"])
        db.session.add(task)
        db.session.commit()
        return jsonify(task.to_dict(),201)
    
    @app.route("/tasks",methods=["GET"])
    def get_tasks():
        tasks = Task.query.all()
        return jsonify([task.to_dict() for task in tasks])
    
    @app.route("/tasks/<int:task_id>",methods = ["PUT"])
    def update_task(task_id):
        task = Task.query.get_or_404(task_id)
        data = request.get_json()
        task.title = data.get("title",task.title)
        task.completed = data.get("completed",task.completed)
        db.session.commit()
        return jsonify(task.to_dict())

    @app.route("/tasks/<int:task_id>",methods = ["DELETE"])
    def delete_task(task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message":"Deleted"})
