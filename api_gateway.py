# api_gateway.py
from flask import Blueprint, jsonify, request
import requests
import io
import sys

# Create a Blueprint for the API gateway
gateway_app = Blueprint('gateway_app', __name__)

# Redirect stdout to a StringIO object
stdout = sys.stdout
sys.stdout = io.StringIO()

# Define the routes and their corresponding backend services
routes = {
    '/users': 'https://jsonplaceholder.typicode.com/users',
    '/products': 'https://reqres.in/api/products',
    '/orders': 'https://jsonplaceholder.typicode.com/orders'
}

# Example route for GET /users
@gateway_app.route('/users', methods=['GET'])
def get_users():
    users_service_url = routes['/users']
    print(f"\nRequesting users from {users_service_url}")
    response = requests.get(users_service_url)
    print(f"Received response: {response.status_code} {response.text}\n")
    sys.stdout.seek(0)
    output = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = stdout
    return output.replace('\n', '<br>')

# Example route for POST /users
@gateway_app.route('/users', methods=['POST'])
def create_user():
    users_service_url = routes['/users']
    print(f"\nCreating user: {request.json}")
    response = requests.post(users_service_url, json=request.json)
    print(f"Received response: {response.status_code} {response.text}\n")
    sys.stdout.seek(0)
    output = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = stdout
    return output.replace('\n', '<br>')

# Example route for GET /products
@gateway_app.route('/products', methods=['GET'])
def get_products():
    products_service_url = routes['/products']
    print(f"\nRequesting products from {products_service_url}")
    response = requests.get(products_service_url)
    print(f"Received response: {response.status_code} {response.text}\n")
    sys.stdout.seek(0)
    output = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = stdout
    return output.replace('\n', '<br>')

# Example route for POST /products
@gateway_app.route('/products', methods=['POST'])
def create_product():
    products_service_url = routes['/products']
    print(f"\nCreating product: {request.json}")
    response = requests.post(products_service_url, json=request.json)
    print(f"Received response: {response.status_code} {response.text}\n")
    sys.stdout.seek(0)
    output = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = stdout
    return output.replace('\n', '<br>')

# Example route for GET /orders
@gateway_app.route('/orders', methods=['GET'])
def get_orders():
    orders_service_url = routes['/orders']
    print(f"\nRequesting orders from {orders_service_url}")
    response = requests.get(orders_service_url)
    print(f"Received response: {response.status_code} {response.text}\n")
    sys.stdout.seek(0)
    output = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = stdout
    return output.replace('\n', '<br>')

# Example route for POST /orders
@gateway_app.route('/orders', methods=['POST'])
def create_order():
    orders_service_url = routes['/orders']
    print(f"\nCreating order: {request.json}")
    response = requests.post(orders_service_url, json=request.json)
    print(f"Received response: {response.status_code} {response.text}\n")
    sys.stdout.seek(0)
    output = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = stdout
    return output.replace('\n', '<br>')