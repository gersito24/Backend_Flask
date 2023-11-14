from utils.ma import ma
from models.solicitud import Solicitud

class SolicitudSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Solicitud
        fields = ('id_solicitud', 'id_predio', 'id_solicitante', 'id_servicio', 'area_predio', 'num_casas', 'cant_acomunes', 'area_acomunes', 'cant_vigilantes', 'cant_plimpieza', 'cant_administracion', 'cant_jardineria', 'fecha_solicitud', 'nombre_solicitante')

solicitud_schema = SolicitudSchema()
solicitudes_schema = SolicitudSchema(many=True)