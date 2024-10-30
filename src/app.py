#servidor básico en flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, Mundo! Este es un servidor Flask."

if __name__ == "__main__":
    app.run(debug=True)
