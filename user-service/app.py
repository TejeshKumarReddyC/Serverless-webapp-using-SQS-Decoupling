from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    return jsonify({"message": f"User {username} registered"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    return jsonify({"token": f"dummy-token-for-{username}"}), 200

@app.route('/health', methods=['GET'])
def health():
    return "User service is Healthy", 200
