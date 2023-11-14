from utils.ma import ma

class InformacionSolicitudSchema(ma.Schema):
    class Meta:
        fields = ('numero de solicitud', 'id_solicitante', 'id_persona', 'id_predio', 'nombre solicitante', 'fecha_solicitud', 'predio', 'area del predio', 'numero de casas', 'servicio solicitado', 'cantidad de areas comunes', 'id_area_comun', 'id_predio_area_comun')

informacion_solicitud_schema = InformacionSolicitudSchema()
informacion_solicitud_schemas = InformacionSolicitudSchema(many=True)