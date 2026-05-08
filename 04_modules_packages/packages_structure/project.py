"""
PROJECT: The Enterprise Logger

Goal: Create a logging package.

Structure:
logger/
├── __init__.py (Exposes 'log' function)
├── handlers/
│   ├── __init__.py
│   ├── console.py (prints to screen)
│   └── file.py (writes to a log.txt)
└── formatter.py (formats the message with a timestamp)

Requirement:
- Importing 'logger' should allow the user to call:
  logger.log("message", destination="console")
"""

# TODO: Implement the project

import os
import sys

# Directory where this script exists
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Add this directory to Python path
sys.path.append(BASE_DIR)

# Create logger package structure
logger_dir = os.path.join(BASE_DIR, "logger")
handlers_dir = os.path.join(logger_dir, "handlers")

os.makedirs(handlers_dir, exist_ok=True)

# __init__.py
with open(os.path.join(logger_dir, "__init__.py"), "w") as f:
    f.write(
        "from .formatter import format_message\n"
        "from .handlers.console import log_to_console\n"
        "from .handlers.file import log_to_file\n\n"
        "def log(message, destination='console'):\n"
        "    formatted = format_message(message)\n\n"
        "    if destination == 'console':\n"
        "        log_to_console(formatted)\n"
        "    elif destination == 'file':\n"
        "        log_to_file(formatted)\n"
        "    else:\n"
        "        print('Invalid destination')\n"
    )

# formatter.py
with open(os.path.join(logger_dir, "formatter.py"), "w") as f:
    f.write(
        "from datetime import datetime\n\n"
        "def format_message(message):\n"
        "    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')\n"
        "    return f'[{timestamp}] {message}'\n"
    )

# handlers/__init__.py
with open(os.path.join(handlers_dir, "__init__.py"), "w") as f:
    f.write("# Handlers Package\n")

# handlers/console.py
with open(os.path.join(handlers_dir, "console.py"), "w") as f:
    f.write(
        "def log_to_console(message):\n"
        "    print(message)\n"
    )

# handlers/file.py
with open(os.path.join(handlers_dir, "file.py"), "w") as f:
    f.write(
        "def log_to_file(message):\n"
        "    with open('log.txt', 'a') as file:\n"
        "        file.write(message + '\\n')\n"
    )

# Import logger package
import logger

# Test console logging
logger.log("System started", destination="console")

# Test file logging
logger.log("This is saved in the file", destination="file")

print("Enterprise Logger Project initialized.")