from flask import Flask, request, jsonify

app = Flask(__name__)

# CRUD: Create, Read, Update, Delete
tasks = []
task_id_control = 1

@app.route("/tasks", methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new = {
        "id": task_id_control,
        "title": data.get("title"),
        "description": data.get("description", "")
    }
    tasks.append(new)
    task_id_control += 1
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"}), 201

@app.route("/tasks", methods=['GET'])
def get_tasks():
    return jsonify({
        "tasks": tasks,
        "total_tasks": len(tasks)
    }), 200

@app.route("/tasks/<int:id>", methods=['GET'])
def get_task(id):
    task = next((t for t in tasks if t['id'] == id), None)
    if task:
        return jsonify(task), 200
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
