from utils.ma import ma
from models.predio_area_comun import PredioAreaComun

class PredioAreaComunSchema(ma.SQLAlchemySchema):
    class Meta:
        model = PredioAreaComun
        fields = ('id_predio', 'id_area_comun', 'codigo', 'area')

predioAreaComun_schema = PredioAreaComunSchema()
prediosAreaComun_schema = PredioAreaComunSchema(many=True)