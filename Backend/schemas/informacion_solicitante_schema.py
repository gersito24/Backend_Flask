# schemas/informacion_solicitante_schema.py
from utils.ma import ma

class InformacionSolicitanteSchema(ma.Schema):
    class Meta:
        fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'tipo_documento', 'numero_documento', 'ubicacion', 'numero_contacto', 'direccion', 'correo')

informacion_solicitante_schema = InformacionSolicitanteSchema()
informacion_solicitante_schemas = InformacionSolicitanteSchema(many=True)
