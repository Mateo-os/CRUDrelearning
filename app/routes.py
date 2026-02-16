from flask import request, jsonify
from app.services.task_services import (
    create_task,
    get_tasks,
    get_task_by_id,
    update_task,
    delete_task
)

def register_routes(app):

    @app.route("/tasks",methods=["POST"])
    def create():
        data = request.get_json()

        if not data or "title" not in data:
            return jsonify({"error": "Title is required"}), 400
        
        task = create_task(data["title"])
        return jsonify(task.to_dict(),201)
        
    @app.route("/tasks",methods=["GET"])
    def get_all():
        page = request.args.get("page",1,type=int)
        limit = request.args.get("limit",10,type=int)
        
        pagination = get_tasks(page,limit)
        
        return jsonify({
            "items": [task.to_dict() for task in pagination.items],
            "total": pagination.total,
            "page": pagination.page,
            "pages": pagination.pages
        })
    
    @app.route("/tasks/<int:task_id>",methods = ["PUT"])
    def update(task_id):
        task = get_task_by_id(task_id)
        data = request.get_json()
        updated = update_task(
            task,
            title = data.get("title"),
            completed=data.get("completed")
        )
        return jsonify(updated.to_dict())

    @app.route("/tasks/<int:task_id>",methods = ["DELETE"])
    def delete(task_id):
        task = get_task_by_id(task_id)
        delete_task(task)
        return jsonify({"message":"Deleted"})
