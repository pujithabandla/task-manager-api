from flask import Blueprint, jsonify, request
from models.task import db, Task

task_bp = Blueprint('task_bp', __name__)

@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{
        "id": t.id,
        "title": t.title,
        "description": t.description,
        "done": t.done
    } for t in tasks])