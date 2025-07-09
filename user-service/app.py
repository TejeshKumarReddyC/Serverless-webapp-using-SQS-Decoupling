from flask import Flask, jsonify, request
from werkzeug.middleware.dispatcher import DispatcherMiddleware

flask_app = Flask(__name__)

@flask_app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return jsonify({"token": "dummy-token-for-" + data.get("username")})

@flask_app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return jsonify({"message": f"User {data.get('username')} registered"}), 201

@flask_app.route('/health', methods=['GET'])
def health():
    return "User service healthy", 200

# Dispatcher to map /user prefix
app = DispatcherMiddleware(Flask('dummy_root'), {
    '/user': flask_app
})
