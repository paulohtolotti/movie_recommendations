from flask import Flask, request, jsonify
from controller_filmes import recomendar

app = Flask(__name__)

@app.route("/recomendar", methods=["GET"])
def recomendar_api():
    nome_filme = request.args.get("filme")
    if not nome_filme:
        return jsonify({"erro": "Informe um filme"}), 400
    
    try:
        resultados = recomendar(nome_filme)
        return jsonify({"filme": nome_filme, "recomendacoes": resultados.tolist()})
    except KeyError:
        return jsonify({"erro": "Filme nao encontrado"}), 404
        

if __name__ == "__main__":
    app.run(debug=True)
