import sys
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from Files.Scripts.python.scheduler.inactivity_tracker import update_last_access
from Files.Scripts.python.endpoints.validar_servicio import Start_Rclone

# ===== Validaciones iniciales
load_dotenv()
sys.stdout = sys.stderr

# ===== Configuracion API
app = Flask(__name__)
CORS(app)
api = Api(app)

# ===== Middleware para actualizar la hora del último acceso en cada request
@app.before_request
def before_request():
    update_last_access()

# ===== Endpoints
api.add_resource(Start_Rclone, '/start')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
