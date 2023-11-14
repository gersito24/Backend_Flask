from utils.ma import ma
from models.solicitante import Solicitante

class SolicitanteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Solicitante
        fields = ('id_solicitante', 'id_persona', 'id_rol', 'telefono', 'correo')

solicitante_schema = SolicitanteSchema()
solicitantes_schema = SolicitanteSchema(many=True)