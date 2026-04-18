from flask import Blueprint, jsonify, request
from models.task import db, Task

task_bp = Blueprint('task_bp', __name__)


@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "done": t.done
        } for t in tasks
    ])


@task_bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "done": task.done
    })


@task_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    new_task = Task(
        title=data["title"],
        description=data["description"]
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Task created"}), 201


@task_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.done = data.get("done", task.done)

    db.session.commit()

    return jsonify({"message": "Task updated"})


@task_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted"})