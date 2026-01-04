from cryptography.fernet import Fernet

KEY_FILE = "key.key"
LOG_FILE = "logs.enc"

with open(KEY_FILE, "rb") as f:
    key = f.read()

cipher = Fernet(key)

with open(LOG_FILE, "rb") as f:
    for line in f:
        decrypted = cipher.decrypt(line.strip())
        print(decrypted.decode())
