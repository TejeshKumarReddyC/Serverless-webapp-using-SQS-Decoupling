from flask import Flask, jsonify, request
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import boto3, os, json

flask_app = Flask(__name__)

sqs = boto3.client("sqs", region_name="ap-south-1")
queue_url = os.environ.get("ORDER_QUEUE_URL", "")

@flask_app.route('/order', methods=['POST'])
def place_order():
    data = request.get_json()
    sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(data))
    return jsonify({"message": "Order placed successfully"}), 201

@flask_app.route('/orders', methods=['GET'])
def list_orders():
    return jsonify([{"id": 1, "product_id": 1, "status": "confirmed"}])

@flask_app.route('/health', methods=['GET'])
def health():
    return "Order service healthy", 200

# Dispatcher to map /order prefix
app = DispatcherMiddleware(Flask('dummy_root'), {
    '/order': flask_app
})
