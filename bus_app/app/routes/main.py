from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app import db
from app.models.user import FavoriteRoute

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('main/index.html')

@bp.route('/api/favorites', methods=['GET', 'POST', 'DELETE'])
@login_required
def handle_favorites():
    if request.method == 'GET':
        favorites = FavoriteRoute.query.filter_by(user_id=current_user.id).all()
        return jsonify([{'id': f.id, 'route_id': f.route_id} for f in favorites])
    elif request.method == 'POST':
        route_id = request.json.get('route_id')
        if route_id:
            new_favorite = FavoriteRoute(route_id=route_id, user_id=current_user.id)
            db.session.add(new_favorite)
            db.session.commit()
            return jsonify({'message': 'Favorite added successfully'}), 201
        return jsonify({'error': 'Invalid route_id'}), 400
    elif request.method == 'DELETE':
        route_id = request.json.get('route_id')
        if route_id:
            favorite = FavoriteRoute.query.filter_by(user_id=current_user.id, route_id=route_id).first()
            if favorite:
                db.session.delete(favorite)
                db.session.commit()
                return jsonify({'message': 'Favorite removed successfully'}), 200
            return jsonify({'error': 'Favorite not found'}), 404
        return jsonify({'error': 'Invalid route_id'}), 400

@bp.route('/favorites')
@login_required
def favorites_page():
    return render_template('main/favorites.html')
