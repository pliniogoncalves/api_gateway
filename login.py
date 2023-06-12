# login.py

from flask import jsonify, request
from api_gateway import routes
import requests

def login():
    username = request.json.get("username")
    password = request.json.get("email")

    users_service_url = routes['/users']

    response = requests.get(users_service_url)
    users = response.json()

    for user in users:
        if user["username"] == username and user["email"] == password:
            return jsonify(message='Login successful')

    return jsonify(message='Invalid credentials'), 401
