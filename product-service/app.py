from flask import Flask, jsonify, request
from werkzeug.middleware.dispatcher import DispatcherMiddleware

flask_app = Flask(__name__)

@flask_app.route('/products', methods=['GET'])
def list_products():
    return jsonify([
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Phone"}
    ])

@flask_app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    return jsonify({"message": f"Product '{data.get('name')}' added"}), 201

@flask_app.route('/health', methods=['GET'])
def health():
    return "Product service healthy", 200

# Dispatcher to map /product prefix
app = DispatcherMiddleware(Flask('dummy_root'), {
    '/product': flask_app
})
