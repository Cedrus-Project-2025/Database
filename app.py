import os, sys
from dotenv import load_dotenv
from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS

# ===== Validaciones iniciales
load_dotenv()
sys.stdout = sys.stderr

# ===== Configuracion API
app = Flask(__name__)
CORS(app)
api = Api(app)


# ===== Endpoints




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)