from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.json.get('todo')
    if todo:
        todos.append(todo)
        return jsonify({'message': 'Todo added!'}), 201
    return jsonify({'message': 'Todo is required!'}), 400

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        todos.pop(todo_id)
        return jsonify({'message': 'Todo deleted!'}), 200
    return jsonify({'message': 'Invalid todo ID!'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

