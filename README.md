# Ethical Keylogger (WSL-Compatible)

## Important Ethical Notice

This project is strictly for **educational and defensive security purposes**.

* Run only on your own machine
* No network access or data exfiltration
* All logs are encrypted locally
* Do not use on systems you do not own or administer

The goal of this project is to demonstrate how keylogging works **and** how modern operating systems restrict it.

---

## Project Overview

This is a WSL-compatible, terminal-focused input monitoring tool written in Python.

Because Windows Subsystem for Linux (WSL) does not expose global keyboard events to Linux processes, this project captures **only keystrokes entered while the program is in focus**. This behavior is intentional and highlights modern OS-level security protections against keylogging.

---

## Features

* Encrypted keystroke logging using Fernet (AES)
* Explicit start and stop controls
* No background or hidden execution
* Fully functional inside WSL
* Demonstrates OS-level mitigations against keylogging

---

## Project Structure

```
ethical_keylogger/
├── generate_key.py    # Generates the encryption key (run once)
├── key.key            # Encryption key (required to decrypt logs)
├── keylogger.py       # Global keylogger (Windows / X11 only)
├── wsl_keylogger.py   # WSL-compatible input monitor
├── view_logs.py       # Decrypts and displays logs
├── logs.enc           # Encrypted keystroke logs
└── venv/              # Python virtual environment
```

---

## Requirements

* Windows with WSL enabled
* Python 3.10 or newer
* pip

Python libraries (installed in a virtual environment):

* cryptography
* pynput (used only for non-WSL environments)

---

## Setup Instructions

### 1. Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```
pip install cryptography pynput
```

---

## Generate the Encryption Key (Run Once)

This step creates the encryption key used to secure keystroke logs.

```
python3 generate_key.py
```

Do not regenerate this key unless you intentionally want to lose access to existing logs.

---

## Running the Project in WSL

Use the WSL-compatible logger:

```
python3 wsl_keylogger.py
```

### Controls

* F8: Start / stop logging
* ESC: Exit the program safely

Keystrokes are logged only while the program window is active. This limitation is enforced by WSL for security reasons.

---

## Viewing (Decrypting) Logs

All keystrokes are stored in encrypted form in `logs.enc`.

To decrypt and view the logs:

```
python3 view_logs.py
```

Example output:

```
2026-01-04 20:22:11.123456 | h
2026-01-04 20:22:11.301234 | e
2026-01-04 20:22:11.489012 | l
```

---

## Defensive Security Explanation

This project demonstrates why modern platforms such as WSL prevent traditional keylogging techniques.

Key takeaways:

* Global keyboard capture is blocked in WSL by design
* Linux processes in WSL cannot access raw input devices
* This significantly reduces the risk of credential harvesting
* Attackers therefore favor environments with weaker input isolation

The project intentionally respects these constraints to highlight real-world defensive controls rather than bypass them.

---

## What I Learned

* How keyloggers operate at a technical level
* How encryption protects sensitive data at rest
* Why WSL, Wayland, and modern OS designs block global input capture
* How OS-level mitigations reduce the effectiveness of common malware techniques
* How to design security tooling that is ethical and controlled

---

## Portfolio Usage

Suggested description:

"This project explores how modern operating systems restrict global keyboard capture and demonstrates an encrypted, controlled input-monitoring tool designed to highlight OS-level defenses against keylogging."

---

## License

Educational use only.
Do not deploy on systems you do not own or manage.

---

## Status

Fully functional in WSL
Ethical by design
Suitable for cybersecurity and IT portfolios
