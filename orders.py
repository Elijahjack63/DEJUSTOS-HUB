# orders.py
from flask import Blueprint, request, jsonify
import uuid
import json
import os
from datetime import datetime

orders_bp = Blueprint('orders', __name__)

ORDERS_FILE_PATH = 'data/orders.json'

@orders_bp.route('/api/admin/orders', methods=['GET'])
def get_all_orders():
    date_filter = request.args.get('date')       # e.g. 2025-05-14
    category_filter = request.args.get('category')  # e.g. "Herbal Supplement"

    orders = []
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, 'r') as f:
            for line in f:
                try:
                    order = json.loads(line.strip())
                    created_at = order.get('createdAt', '')[:10]  # ISO format → just date part

                    # Apply date filter
                    if date_filter and created_at != date_filter:
                        continue

                    # Apply category filter
                    if category_filter:
                        found = False
                        for item in order.get('items', []):
                            if item.get('category') == category_filter:
                                found = True
                                break
                        if not found:
                            continue

                    orders.append(order)
                except json.JSONDecodeError:
                    continue  # Skip bad lines

    return jsonify(orders)

@orders_bp.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json()

    # Validate basic structure
    if not data or 'customer' not in data or 'items' not in data or 'total' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    order_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    order = {
        'id': order_id,
        'customer': data['customer'],
        'items': data['items'],
        'total': data['total'],
        'createdAt': timestamp
    }

    try:
        with open('orders.json', 'a') as f:
            f.write(json.dumps(order) + '\n')
    except Exception as e:
        return jsonify({'error': f'Failed to save order: {str(e)}'}), 500

    return jsonify({'message': 'Order placed successfully', 'orderId': order_id}), 201
