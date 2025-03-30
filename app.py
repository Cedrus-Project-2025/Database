import sys, os
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

# ===== General
from Files.Scripts.python.scheduler.inactivity_tracker import update_last_access
from Files.Scripts.python.endpoints.validar_servicio import Start_Rclone
from Files.Scripts.python.endpoints.tablas import Tables
from Files.Scripts.python.endpoints.registros import Registers


# ===== Validaciones iniciales
load_dotenv()
sys.stdout = sys.stderr
location_path = os.path.dirname(__file__)

# ===== Configuracion API
app = Flask(__name__)
CORS(app)
api = Api(app)
Start_Rclone().start()

# ===== Middleware para actualizar la hora del último acceso en cada request
@app.before_request
def before_request():
    update_last_access()
    

# ===== Endpoints
# General
api.add_resource(Tables,     '/general/tables', endpoint = 'general_tables')
api.add_resource(Registers,  '/general/registers', endpoint = 'general_registers')

# Business
api.add_resource(Tables,     '/business/tables', endpoint = 'business_tables')
api.add_resource(Registers,  '/business/registers', endpoint = 'business_registers')

# Chat
api.add_resource(Tables,     '/chat/tables', endpoint = 'chat_tables')
api.add_resource(Registers,  '/chat/registers', endpoint = 'chat_registers')

# Web
api.add_resource(Tables,     '/web/tables', endpoint = 'web_tables')
api.add_resource(Registers,  '/web/registers', endpoint = 'web_registers')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
