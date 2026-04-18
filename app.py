from flask import Flask
from models.task import db
from routes.task_routes import task_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(task_bp)


@app.route("/")
def home():
    return {"message": "Task Manager API (structured) running"}


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    import os
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))