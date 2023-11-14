# schemas/estado_solicitud_schema.py
from utils.ma import ma
from models.estado_solicitud import EstadoSolicitud
from models.solicitud_estado_solicitud import SolicitudEstadoSolicitud

class ConteoEstadoSolicitudSchema(ma.SQLAlchemySchema):
    class Meta:
        model = SolicitudEstadoSolicitud
        fields = ('estado_solicitud', 'cantidad')

conteo_estado_solicitud_schema = ConteoEstadoSolicitudSchema()
conteo_estado_solicitud_schemas = ConteoEstadoSolicitudSchema(many=True)
