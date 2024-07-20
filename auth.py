import jwt
import datetime
from functools import wraps
import streamlit as st

SECRET_KEY = 'your_secret_key'

def generate_token(username):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        'iat': datetime.datetime.utcnow(),
        'sub': username
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = st.session_state.get('token')
        if not token or decode_token(token) is None:
            st.warning('Veuillez vous connecter pour accéder à cette page.')
            st.stop()
        return f(*args, **kwargs)
    return decorated_function

def authenticate(username, password):
    # Ajoutez ici votre logique d'authentification (vérifiez les informations d'identification dans la base de données ou ailleurs)
    valid_users = {
        'client1': 'password1',
        'client2': 'password2'
    }
    if username in valid_users and valid_users[username] == password:
        return True
    return False
