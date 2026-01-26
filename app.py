
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # Resposta simples para facilitar os testes e o CI
    return "Hello World", 200


if __name__ == "__main__":
    app.run(debug=True)
