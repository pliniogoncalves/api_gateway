# auth.py
def authenticate_user(username, password):
    # logica de autenticação
    if username == 'admin' and password == 'password':
        return True
    return False