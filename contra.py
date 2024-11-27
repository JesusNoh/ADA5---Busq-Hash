import hashlib
import secrets

def hash_password(password):
    salt = secrets.token_hex(16)
    hash_object = hashlib.sha256((password + salt).encode())
    hash_hex = hash_object.hexdigest()
    return salt, hash_hex

user_password = input("Ingresa tu contraseña: ")
salt, hashed_password = hash_password(user_password)

print(f"Salt: {salt}")
print(f"Hash de la contraseña: {hashed_password}")