from flask import Flask, request, jsonify, gunicorn

app = Flask(__name__)

tarefas = [
    {
        "id": 1,
        "titulo": "Lavar a louça",
        "descricao": "Lavar a louça para deixar a cozinha limpa e organizada",
        "status": "Em andamento",
        "prioridade": "Alta",
        "categoria": "Casa",
        "prazo": "Hoje"
    },
    {
        "id": 2,
        "titulo": "Estudar ENEM",
        "descricao": "Estudar para o ENEM e entrar na faculdade de psicologia",
        "status": "A começar",
        "prioridade": "Média",
        "categoria": "Educação",
        "prazo": "Próxima semana"
    }
]


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tarefas)


@app.route('/task/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    tarefa = next((t for t in tarefas if t["id"] == task_id), None)
    return jsonify(tarefa) if tarefa else ("Tarefa não encontrada", 404)


@app.route('/tasks', methods=['POST'])
def create_task():
    nova_tarefa = request.json
    nova_tarefa['id'] = tarefas[-1]['id'] + 1 if tarefas else 1
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201


@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    tarefa = next((t for t in tarefas if t["id"] == task_id), None)
    if not tarefa:
        return "Tarefa não encontrada", 404

    dados = request.json
    tarefa.update(dados)
    return jsonify(tarefa)


@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tarefas
    tarefas = [t for t in tarefas if t["id"] != task_id]
    return "Tarefa removida com sucesso", 200


if __name__ == '__main__':
    app.run(debug=True)
