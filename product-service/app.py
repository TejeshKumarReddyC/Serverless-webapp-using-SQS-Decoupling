from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/products', methods=['GET'])
def list_products():
    return jsonify([
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Phone"}
    ])

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    return jsonify({"message": f"Product '{data.get('name')}' added"}), 201
