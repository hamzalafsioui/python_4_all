"""
PROJECT: The Dependency Checker

Goal: Create a script that checks if a list of required packages are installed.

Requirements:
1. Create a 'requirements.txt' with:
   requests==2.28.1
   colorama==0.4.5
2. Write a script 'project.py' that reads this file and checks if each 
   package is available using 'importlib.util.find_spec'.
3. Print a report of which packages are missing.
"""

import importlib.util

# TODO: Implement the checker
print("Dependency Checker Project initialized.")
