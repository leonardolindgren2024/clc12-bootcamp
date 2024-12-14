from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Leonardo-Lindgren v1.0"