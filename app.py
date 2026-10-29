
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/mensagem", methods=["POST"])
def mensagem():
    return jsonify({
        "resultado": "Olá! O Python foi executado com sucesso!"
    })


@app.route("/somar", methods=["POST"])
def somar():
    dados = request.get_json()

    try:
        numero1 = float(dados["numero1"])
        numero2 = float(dados["numero2"])

        resultado = numero1 + numero2

        return jsonify({
            "resultado": resultado
        })

    except (ValueError, TypeError, KeyError):
        return jsonify({
            "erro": "Digite dois números válidos."
        }), 400


if __name__ == "__main__":
    app.run(debug=True)