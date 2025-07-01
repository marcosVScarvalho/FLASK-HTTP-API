from flask import Flask, request
from models.task import Task

app = Flask(__name__)

# CRUD
# Create, Read, Updat and Delete = Criar, Ler, Atualizar e Deletar
# Tabela: Tarefa

tasks = []

@app.route("/tasks" , methods=['POST'])
def create_task():
    data = request.get_json()
    print(data)
    return "Test"


if __name__ == "__main__":
    app.run(debug=True)