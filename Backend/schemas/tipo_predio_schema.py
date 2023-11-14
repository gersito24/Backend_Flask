from utils.ma import ma
from models.tipo_predio import TipoPredio

class TipoPredioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = TipoPredio
        fields = ('id_tipo_predio', 'nomre_predio')

tipoPredio_schema = TipoPredioSchema()
tiposPredio_schema = TipoPredioSchema(many=True)