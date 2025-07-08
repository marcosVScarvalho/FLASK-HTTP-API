from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD: Create, Read, Update, Delete
tasks = []
task_id_control = 1

@app.route("/tasks", methods=['POST'])
def create_tasks():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data["title"], description=data.get("description"), completed=False)
    new = {
        "id": task_id_control,
        "title": data.get("title"),
        "description": data.get("description", "")
    }
    tasks.append(new)
    task_id_control += 1
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id}), 200

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
    return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404

@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = None
    for t in tasks:
        if t['id'] == id: 
            task = t
            break 

    if task is None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    data = request.get_json()
    task['title'] = data.get('title', task['title'])
    task['description'] = data.get('description', task.get('description', ''))
    task['completed'] = data.get('completed', task.get('completed', False))
    return jsonify({"message": "Tarefa atualizada com sucesso"}), 200

@app.route("/tasks/<int:id>", methods=['DELETE'])
def delete_task(id):
    task = next((t for t in tasks if t['id'] == id), None)
    if not task:
        print("Tarefa não encontrada", tasks)
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa doi deletada com sucesso"}), 200
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)