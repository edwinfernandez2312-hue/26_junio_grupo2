from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return {
        "mensaje": "API de ventas operativa"
    }

@app.route("/estado")
def estado():
    return {
        "mensaje": "Servicio funcionando correctamente",
        "estado": "activo"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)