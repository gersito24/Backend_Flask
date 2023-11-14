from utils.ma import ma
from models.tipo_documento import TipoDocumento

class TipoDocumentoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = TipoDocumento
        fields = ('id_tipo_documento', 'descripcion')

tipoDocumento_schema = TipoDocumentoSchema()
tiposDocumento_schema = TipoDocumentoSchema(many=True)
