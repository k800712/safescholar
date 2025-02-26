from functools import wraps
from flask import jsonify

class APIError(Exception):
    pass

def handle_api_error(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except APIError as e:
            return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": "An unexpected error occurred"}), 500
    return decorated_function
