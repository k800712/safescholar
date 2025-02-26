from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    favorite_routes = db.relationship('FavoriteRoute', backref='user', lazy=True)

class FavoriteRoute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

