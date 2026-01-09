import curses
from datetime import datetime
from cryptography.fernet import Fernet
import os

LOG_FILE = "logs.enc"
KEY_FILE = "key.key"

# Load encryption key
with open(KEY_FILE, "rb") as f:
    key = f.read()

cipher = Fernet(key)

def save(entry):
    encrypted = cipher.encrypt(entry.encode())
    with open(LOG_FILE, "ab") as f:
        f.write(encrypted + b"\n")

def main(stdscr):
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(False)

    logging_enabled = False

    stdscr.clear()
    stdscr.addstr(0, 0, "WSL Ethical Input Monitor")
    stdscr.addstr(2, 0, "F8  = Start / Stop logging")
    stdscr.addstr(3, 0, "ESC = Exit")
    stdscr.addstr(5, 0, "Status: LOGGING OFF")
    stdscr.refresh()

    while True:
        key = stdscr.getch()

        if key == 27:  # ESC
            break

        if key == curses.KEY_F8:
            logging_enabled = not logging_enabled
            status = "LOGGING ON" if logging_enabled else "LOGGING OFF"
            stdscr.addstr(5, 0, f"Status: {status}      ")
            stdscr.refresh()
            continue

        if logging_enabled:
            try:
                char = chr(key)
            except ValueError:
                char = f"[{key}]"

            entry = f"{datetime.now()} | {char}"
            save(entry)

    stdscr.clear()
    stdscr.addstr(0, 0, "Exiting safely...")
    stdscr.refresh()

curses.wrapper(main)
