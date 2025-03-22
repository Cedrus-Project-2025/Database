from flask import Flask, jsonify
from Files.Scripts.python.inactivity_tracker import update_last_access

app = Flask(__name__)

# Middleware para actualizar la hora del último acceso en cada request
@app.before_request
def before_request():
    update_last_access()

# Ruta principal para verificar que el servidor está activo
@app.route("/")
def index():
    return {"message": "API en funcionamiento", "status": "ok"},200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
