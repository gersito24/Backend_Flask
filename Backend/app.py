from flask import Flask
from routes.persona_routes import persona_routes
from routes.rol_routes import rol_routes
from routes.solicitante_routes import solicitante_routes
from routes.solicitud_routes import solicitud_routes
from routes.tipo_documento_routes import tipo_documento_routes
from routes.predio_routes import predio_routes
from routes.servicio_routes import servicio_routes
from routes.tipo_predio_routes import tipo_predio_routes
from routes.ubigeo_routes import ubigeo_routes
from routes.personal_routes import personal_routes
from routes.area_comun_routes import area_comun_routes
from routes.predio_area_comun_routes import predio_area_comun_routes
from routes.estado_solicitud_routes import estado_solicitud_routes
from routes.conteo_estado_solicitud_routes import conteo_estado_solicitud_routes
from routes.solicitudes_estado_routes import solicitudes_estado_routes
from routes.informacion_solicitante_routes import informacion_solicitante_routes
from routes.informacion_solicitud_routes import informacion_solicitud_routes
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI
from flask_cors import CORS
from utils.db import db

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = 'clavesecreta123'

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db.init_app(app)

app.register_blueprint(persona_routes)
app.register_blueprint(rol_routes)
app.register_blueprint(solicitante_routes)
app.register_blueprint(solicitud_routes)
app.register_blueprint(tipo_documento_routes)
app.register_blueprint(predio_routes)
app.register_blueprint(servicio_routes)
app.register_blueprint(tipo_predio_routes)
app.register_blueprint(ubigeo_routes)
app.register_blueprint(personal_routes)
app.register_blueprint(area_comun_routes)
app.register_blueprint(predio_area_comun_routes)
app.register_blueprint(estado_solicitud_routes)
app.register_blueprint(conteo_estado_solicitud_routes)

app.register_blueprint(solicitudes_estado_routes)
app.register_blueprint(informacion_solicitante_routes)
app.register_blueprint(informacion_solicitud_routes)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

