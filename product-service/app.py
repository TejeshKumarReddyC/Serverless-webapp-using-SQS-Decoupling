from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory list for demo purposes
products = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Phone"}
]

@app.route('/products', methods=['GET'])
def list_products():
    return jsonify(products), 200

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    product_name = data.get('name')
    new_id = len(products) + 1
    new_product = {"id": new_id, "name": product_name}
    products.append(new_product)
    return jsonify({"message": f"Product '{product_name}' added"}), 201

@app.route('/health', methods=['GET'])
def health():
    return "Product service is healthy", 200
