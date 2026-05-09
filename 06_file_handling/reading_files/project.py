"""
PROJECT: Simple Log Analyzer

Goal: Read a log file and extract specific information.

Instructions:
1. Create a file 'system.log' with the following content:
   INFO: System started
   DEBUG: Checking database
   ERROR: Connection failed
   INFO: User logged in
   ERROR: Disk full

2. Write a script that:
   - Reads 'system.log'.
   - Counts how many "INFO", "DEBUG", and "ERROR" messages exist.
   - Prints only the "ERROR" messages to the console.
"""

# TODO: Implement the log analyzer

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "system.log")

with open(FILE_PATH, "r") as f:
    content = f.read()
    print(content)

    # total number of "INFO" messages
    print("total number of INFO messages: ",content.count("INFO"))

    # total number of "DEBUG" messages
    print("total number of DEBUG messages: ",content.count("DEBUG"))

    # total number of "ERROR" messages
    print("total number of ERROR messages: ",content.count("ERROR"))

    # print only the "ERROR" messages
    print("ERROR messages: ")

    for line in content.split("\n"):
        if "ERROR" in line:
            print(line)
