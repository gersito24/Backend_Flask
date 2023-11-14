# schemas/estado_solicitud_schema.py
from utils.ma import ma
from models.estado_solicitud import EstadoSolicitud

class EstadoSolicitudSchema(ma.SQLAlchemySchema):
    class Meta:
        model = EstadoSolicitud
        fields = ('id_estado_solicitud', 'descripcion', 'ind_cotizacion')

estado_solicitud_schema = EstadoSolicitudSchema()
estado_solicitudes_schema = EstadoSolicitudSchema(many=True)
