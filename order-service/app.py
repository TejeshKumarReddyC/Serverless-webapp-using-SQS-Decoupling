from flask import Flask, jsonify, request
import boto3, os, json

app = Flask(__name__)

# Initialize SQS
region = "ap-south-1"
sqs = boto3.client("sqs", region_name=region)
queue_url = os.environ.get("ORDER_QUEUE_URL", "")

@app.route('/order', methods=['POST'])
def place_order():
    if not queue_url:
        return jsonify({"error": "ORDER_QUEUE_URL not configured"}), 500

    data = request.get_json()
    try:
        sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(data))
        return jsonify({"message": "Order placed successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/orders', methods=['GET'])
def list_orders():
    return jsonify([
        {"id": 1, "product_id": 1, "status": "confirmed"}
    ]), 200

@app.route('/health', methods=['GET'])
def health():
    return "Order service is healthy", 200
