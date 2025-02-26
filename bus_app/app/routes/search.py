from flask import Blueprint, request, jsonify
from app.services.kakao_search import KakaoSearchService
from app.utils.error_handlers import handle_api_error

bp = Blueprint('search', __name__)

@bp.route('/search/bus_stop', methods=['GET'])
@handle_api_error
def search_bus_stop():
    query = request.args.get('query', '')
    x = request.args.get('x')
    y = request.args.get('y')
    radius = request.args.get('radius', 2000)
    
    search_service = KakaoSearchService()
    results = search_service.search_bus_stop(query, x, y, radius)
    
    return jsonify(results)

@bp.route('/search/bus_route', methods=['GET'])
@handle_api_error
def search_bus_route():
    query = request.args.get('query', '')
    
    search_service = KakaoSearchService()
    results = search_service.search_bus_route(query)
    
    return jsonify(results)

@bp.route('/autocomplete', methods=['GET'])
@handle_api_error
def autocomplete():
    query = request.args.get('query', '')
    
    search_service = KakaoSearchService()
    results = search_service.autocomplete(query)
    
    return jsonify(results)
