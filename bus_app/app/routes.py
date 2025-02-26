from flask import render_template, jsonify, request
from app import app
from app.kakao_api import get_bus_location
from app.models import FavoriteRoute

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/bus_location/<bus_id>')
def bus_location(bus_id):
    location = get_bus_location(bus_id)
    return jsonify(location)

@app.route('/api/autocomplete')
def autocomplete():
    query = request.args.get('q', '')
    # 여기서는 간단한 예시로 고정된 목록을 사용합니다.
    # 실제로는 데이터베이스나 외부 API를 사용하여 결과를 가져와야 합니다.
    all_routes = ["100", "200", "300", "101", "102", "201", "202", "301", "302"]
    results = [route for route in all_routes if query in route]
    return jsonify(results[:10])  # 최대 10개의 결과만 반환
