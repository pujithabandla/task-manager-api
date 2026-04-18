from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Learn Flask",
        "description": "Build first backend API project",
        "done": False
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "Task Manager API is running"
    })


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data or "description" not in data:
        return jsonify({"error": "Title and description are required"}), 400

    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "description": data["description"],
        "done": False
    }

    tasks.append(new_task)
    return jsonify(new_task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            data = request.get_json()

            task["title"] = data.get("title", task["title"])
            task["description"] = data.get("description", task["description"])
            task["done"] = data.get("done", task["done"])

            return jsonify(task), 200

    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted successfully"}), 200

    return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)