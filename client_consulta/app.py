from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)


def carregar_arquivo():
    caminho_arquivo = os.path.join(app.root_path, 'data', 'clients.json')
    try:
        with open(caminho_arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  
    except json.JSONDecodeError:
        return []


def salvar_clientes(clientes):
    os.makedirs(os.path.join(app.root_path, 'data'), exist_ok=True)  
    caminho_arquivo = os.path.join(app.root_path, 'data', 'clients.json')
    with open(caminho_arquivo, 'w') as file:
        json.dump(clientes, file, indent=4)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consulta/<cpf>', methods=['GET'])
def consulta_cliente(cpf):
    clientes = carregar_arquivo()
    cliente = next((c for c in clientes if c['cpf'] == cpf), None)
    
    if cliente:
        return jsonify(cliente)
    else:
        return jsonify({'error': 'Cliente não encontrado'}), 404


@app.route('/cadastro', methods=['POST'])
def cadastro_cliente():
    try:
        novo_cliente = request.get_json()


        if not novo_cliente or 'cpf' not in novo_cliente or 'nome' not in novo_cliente:
            return jsonify({'error': 'Dados inválidos'}), 400

        clientes = carregar_arquivo()

        if any(c['cpf'] == novo_cliente['cpf'] for c in clientes):
            return jsonify({'error': 'CPF já cadastrado'}), 400

        clientes.append(novo_cliente)
        salvar_clientes(clientes)

        return jsonify({'success': 'Cliente cadastrado com sucesso'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
