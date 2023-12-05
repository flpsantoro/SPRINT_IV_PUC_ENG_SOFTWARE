from flask import Blueprint, request, jsonify
import os

upload_blueprint = Blueprint('upload', __name__)

@upload_blueprint.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['modelFile']

    # Verificar se um arquivo foi recebido
    if not file:
        return jsonify(message="Nenhum arquivo recebido.")

    # Verificar se o arquivo é do tipo .pkl
    if not file.filename.endswith('.pkl'):
        return jsonify(message="Tipo de arquivo inválido. Por favor, envie um arquivo .pkl.")

    # Usar o nome original do arquivo
    filename = file.filename
    filepath = os.path.join('models', filename)

    # Salvar o arquivo
    file.save(filepath)
    return jsonify(message=f"Modelo '{filename}' carregado com sucesso.")
