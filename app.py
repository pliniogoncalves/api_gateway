# main.py
from flask import Flask, request, jsonify, render_template
from api_gateway import gateway_app
from login import login
from auth import authenticate_user

app = Flask(__name__)

# Exibir a página index.html
@app.route('/')
def index():
    return render_template('index.html')

# Exibir a página dashboard.html
@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

# Monta os manipuladores de API gateway
app.register_blueprint(gateway_app)

# Define a rota de login
app.add_url_rule('/login', 'login', login, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)

