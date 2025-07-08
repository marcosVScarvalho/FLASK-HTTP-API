# 🗂️ Flask Task Manager API

Projeto de uma API RESTful simples em Flask para gerenciar tarefas, implementando operações básicas de **CRUD**

---

## 📦 Funcionalidades

- **POST /tasks**: criar uma nova tarefa  
- **GET /tasks**: listar todas as tarefas  
- **GET /tasks/<id>**: recuperar uma tarefa específica  
- **PUT /tasks/<id>**: atualizar uma tarefa existente  
- **DELETE /tasks/<id>**: remover uma tarefa  

Cada tarefa possui os campos:
- `id` (inteiro)
- `title` (string)
- `description` (string, opcional)
- `completed` (booleano, opcional — padrão: `False`)

---

## ⚙️ Pré-requisitos

- Python 3.9+  
- Flask (`pip install flask`)  
- (Opcional) `pytest` e `requests` para testes

---

## 🚀 Como rodar o projeto

```bash
# 1. Clone o repositório
git clone https://github.com/marcosVScarvalho/FLASK-HTTP-API.git
cd flask-task-manager

# 2. Instale as dependências
pip install flask

# 3. Execute
python app.py
