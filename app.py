from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD
# Create, Read, Updat and Delete = Criar, Ler, Atualizar e Deletar
# Tabela: Tarefa

tasks = []
task_id_control = 1

@app.route("/tasks" , methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id= task_id_control,title=data.get('title'), description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task.to_dict())
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"})



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)