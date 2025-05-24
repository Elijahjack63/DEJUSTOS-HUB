# auth.py
from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

# Example hardcoded admin user
ADMIN_CREDENTIALS = {
    "email": "admin@gjhub.com",
    "password": "securepassword123"  # In production, never store passwords in plain text
}

@auth_bp.route('/api/admin/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing email or password'}), 400

    email = data['email']
    password = data['password']

    if email == ADMIN_CREDENTIALS['email'] and password == ADMIN_CREDENTIALS['password']:
        return jsonify({'message': 'Login successful'}), 200

    return jsonify({'error': 'Invalid credentials'}), 401

