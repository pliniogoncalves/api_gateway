# auth.py
def authenticate_user(username, password):
    # Perform authentication logic here
    if username == 'admin' and password == 'password':
        return True
    return False