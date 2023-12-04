from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Verifica se a requisição contém um arquivo na chave 'file'
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # Verifica se o nome do arquivo está vazio
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Salva o arquivo binário no disco
    file.save(file.filename or "dummy")

    return jsonify({'message': 'File uploaded successfully'}), 200