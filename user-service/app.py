from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/user/login', methods=['POST'])
def login():
    data = request.get_json()
    return jsonify({"token": "dummy-token-for-" + data.get("username")})

@app.route('/user/register', methods=['POST'])
def register():
    data = request.get_json()
    return jsonify({"message": f"User {data.get('username')} registered"}), 201

@app.route('/health', methods=['GET'])
def health():
    return "User service healthy", 200
