# main.py
from flask import Flask, request, jsonify, render_template
from api_gateway import gateway_app
from auth import authenticate_user

app = Flask(__name__)

# Serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Mount the API gateway handlers
app.register_blueprint(gateway_app)

if __name__ == '__main__':
    app.run(debug=True)

