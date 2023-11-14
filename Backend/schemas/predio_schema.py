from utils.ma import ma
from models.predio import Predio

class PredioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Predio
        fields = ('id_predio', 'id_tipo_predio', 'descripcion', 'ruc', 'telefono', 'correo', 'direccion', 'idubigeo', 'id_persona')

predio_schema = PredioSchema()
predios_schema = PredioSchema(many=True)