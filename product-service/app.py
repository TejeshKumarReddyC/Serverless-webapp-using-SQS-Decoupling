from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/product/products', methods=['GET'])
def list_products():
    return jsonify([
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Phone"}
    ])

@app.route('/product/products', methods=['POST'])
def add_product():
    data = request.get_json()
    return jsonify({"message": f"Product '{data.get('name')}' added"}), 201

@app.route('/health', methods=['GET'])
def health():
    return "Product service healthy", 200
