"""
 Examples: Virtual Environment Commands

This is not a script you run, but a list of commands you use in your terminal.
"""

# 1. Check if you are currently in a virtual environment
import sys
import os

def check_venv():
    # If sys.prefix != sys.base_prefix, you are in a venv
    in_venv = sys.prefix != sys.base_prefix
    print(f"Are we in a virtual environment? {'YES' if in_venv else 'NO'}")
    print(f"Current Python Prefix: {sys.prefix}")
    print(f"Base Python Prefix: {sys.base_prefix}")

if __name__ == "__main__":
    check_venv()
    print("\nTry these commands in your terminal:")
    print("1. python -m venv test_env")
    print("2. test_env\\Scripts\\activate (Windows)")
    print("3. pip list")
    print("4. deactivate")
