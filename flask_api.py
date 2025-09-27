from flask import Flask, jsonify # type: ignore
import json

app = Flask(__name__)

# Rota raiz (página inicial da API)
@app.route("/")
def home():
    return "✅ API rodando! Use /alunos, /saudacao/<nome> ou /curso/<curso>"

# Rota que retorna lista de alunos em JSON
@app.route("/alunos")
def get_alunos():
    alunos = [
        {"nome": "João", "curso": "ADS"},
        {"nome": "Maria", "curso": "CC"},
        {"nome": "Pedro", "curso": "ADS"}
    ]
    # Força o encoding UTF-8 para acentos
    response = jsonify(alunos)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

# Rota que retorna saudação personalizada
@app.route("/saudacao/<nome>")
def saudacao(nome):
    mensagem = {"mensagem": f"Olá, {nome}! Seja bem-vindo à API."}
    response = jsonify(mensagem)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

# Rota que filtra alunos por curso
@app.route("/curso/<curso>")
def filtrar_por_curso(curso):
    alunos = [
        {"nome": "João", "curso": "ADS"},
        {"nome": "Maria", "curso": "CC"},
        {"nome": "Pedro", "curso": "ADS"}
    ]
    
    alunos_filtrados = [aluno for aluno in alunos if aluno["curso"].lower() == curso.lower()]
    
    resultado = {
        "curso": curso,
        "quantidade": len(alunos_filtrados),
        "alunos": alunos_filtrados
    }
    
    response = jsonify(resultado)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)