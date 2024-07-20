import bcrypt

# Liste des mots de passe en clair
passwords = ["yourpassword1", "yourpassword2"]

# Générer les mots de passe hachés
hashed_passwords = [bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') for password in passwords]

# Afficher les mots de passe hachés
for password, hashed in zip(passwords, hashed_passwords):
    print(f"Plain: {password} -> Hashed: {hashed}")
