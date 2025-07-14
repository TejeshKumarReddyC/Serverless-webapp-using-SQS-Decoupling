from flask import Flask, jsonify, request
import boto3, os, json
import logging

app = Flask(__name__)

sqs = boto3.client("sqs", region_name="ap-south-1")
queue_url = os.environ.get("ORDER_QUEUE_URL", "")

@app.route('/order/order', methods=['POST'])
def place_order():
    
    try:
        data = request.get_json()
        logging.info(f"Received order: {data}")
        logging.info(f"Queue URL: {queue_url}")
        
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(data)
        )
        
        logging.info(f"SQS response: {response}")
        return jsonify({"message": "Order placed successfully"}), 201

    except Exception as e:
        logging.error("Exception occurred while placing order", exc_info=True)
        return jsonify({"error": str(e)}), 500


@app.route('/order/orders', methods=['GET'])
def list_orders():
    print(f"Queue URL: {queue_url}")
    return queue_url
    #return jsonify([{"id": 1, "product_id": 1, "status": "confirmed"}])
@app.route('/health', methods=['GET'])
def health():
    return "Order service healthy", 200
