from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.predio_area_comun import PredioAreaComun
from schemas.predio_area_comun_schema import predioAreaComun_schema, prediosAreaComun_schema

predio_area_comun_routes = Blueprint("predio_area_comun_routes", __name__)

@predio_area_comun_routes.route('/predio_area_comun', methods=['POST'])
def create_PredioAreaComun():
    id_predio = request.json.get('id_predio')
    id_area_comun = request.json.get('id_area_comun')
    codigo = request.json.get('codigo')
    area = request.json.get('area')

    new_predio_area_comun = PredioAreaComun(id_predio, id_area_comun, codigo, area)

    db.session.add(new_predio_area_comun)
    db.session.commit()

    result = predioAreaComun_schema.dump(new_predio_area_comun)

    data = {
        'message': 'Nuevo Predio-AreaComun creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@predio_area_comun_routes.route('/predio_area_comun', methods=['GET'])
def get_PrediosAreaComunes():
    all_predios_area_comunes = PredioAreaComun.query.all()
    result = prediosAreaComun_schema.dump(all_predios_area_comunes)

    data = {
        'message': 'Todos los Predios-AreasComunes',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@predio_area_comun_routes.route('/predio_area_comun/<int:id_predio>/<int:id_area_comun>', methods=['GET'])
def get_PredioAreaComun(id_predio, id_area_comun):
    predio_area_comun = PredioAreaComun.query.filter_by(id_predio=id_predio, id_area_comun=id_area_comun).first()

    if not predio_area_comun:
        data = {
            'message': 'Predio-AreaComun no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = predioAreaComun_schema.dump(predio_area_comun)

    data = {
        'message': 'Predio-AreaComun encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@predio_area_comun_routes.route('/predio_area_comun/<int:id_predio>/<int:id_area_comun>', methods=['PUT'])
def update_PredioAreaComun(id_predio, id_area_comun):
    predio_area_comun = PredioAreaComun.query.filter_by(id_predio=id_predio, id_area_comun=id_area_comun).first()

    if not predio_area_comun:
        data = {
            'message': 'Predio-AreaComun no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    codigo = request.json.get('codigo')
    area = request.json.get('area')

    predio_area_comun.codigo = codigo
    predio_area_comun.area = area

    db.session.commit()

    result = predioAreaComun_schema.dump(predio_area_comun)

    data = {
        'message': 'Predio-AreaComun actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@predio_area_comun_routes.route('/predio_area_comun/<int:id_predio>/<int:id_area_comun>', methods=['DELETE'])
def delete_PredioAreaComun(id_predio, id_area_comun):
    predio_area_comun = PredioAreaComun.query.filter_by(id_predio=id_predio, id_area_comun=id_area_comun).first()

    if not predio_area_comun:
        data = {
            'message': 'Predio-AreaComun no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(predio_area_comun)
    db.session.commit()

    data = {
        'message': 'Predio-AreaComun eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)