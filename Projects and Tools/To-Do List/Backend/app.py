from flask import Flask, request, jsonify       # type: ignore
from flask_cors import CORS                     # type: ignore

app = Flask(__name__)
CORS(app)

todos = [
    {"id": 1, "task": "Learn React", "completed":False}
]

@app.route('/todos', methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=["POST"])
def add_todo():
    data = request.json

    new_todo = {
        "id": len(todos) + 1,
        "task": data["task"],
        "completed":False
    }

    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/todos/<int:id>', methods=["PUT"])
def update_todo(id):
    for todo in todos:
        if todo["id"] == id:
            todo["completed"] = not todo["completed"]
            return jsonify(todo)

    return jsonify({"message": "todo not found"}), 404

@app.route('/todos/<int:id>', methods=["DELETE"])
def delete_todo(id):
    global todos
    todos = [todo for todo in todos if todo['id'] != id]
    return jsonify({"message": 'Deleted!'})

if __name__ == '__main__':
    app.run(debug=True)