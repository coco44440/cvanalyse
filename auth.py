import yaml
import bcrypt

# Lire le fichier config.yaml
def load_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

config = load_config()

# Fonction d'authentification
def authenticate(username, password):
    if username in config['credentials']['usernames']:
        stored_password = config['credentials']['usernames'][username]['password']
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            return True
    return False
