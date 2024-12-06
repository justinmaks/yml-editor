from flask import Flask, render_template, request, send_from_directory
import os
import yaml
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

BASE_DIR = "path_to_your_directory"

@app.route('/')
def index():
    file_structure = get_file_structure(BASE_DIR)
    return render_template('index.html', file_structure=file_structure)

@app.route('/file/<path:filename>')
def get_file(filename):
    if filename.endswith(('.yml', '.yaml')):
        file_path = os.path.join(BASE_DIR, filename)
        with open(file_path, 'r') as file:
            content = file.read()
        return render_template('editor.html', filename=filename, content=content)
    return "File type not supported", 400

@socketio.on('save_file')
def save_file(data):
    filename = data.get('filename')
    content = data.get('content')
    file_path = os.path.join(BASE_DIR, filename)
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        emit('save_status', {'status': 'success', 'message': 'File saved successfully'})
    except Exception as e:
        emit('save_status', {'status': 'error', 'message': str(e)})


def get_file_structure(base_dir):
    structure = {}
    for root, dirs, files in os.walk(base_dir):
        rel_path = os.path.relpath(root, base_dir)
        structure[rel_path] = files
    return structure

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
