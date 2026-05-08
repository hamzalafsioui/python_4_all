"""
PROJECT: The System Explorer

Goal: Create a small tool that tells the user about their system.

Instructions:
1. Use 'os' to get the current user's login name.
2. Use 'platform' to get the OS name and version.
3. Use 'datetime' to get the current time.
4. Print a friendly message like:
   "Hello [User]! You are running [OS] on [Current Date/Time]."
"""

# TODO: Implement the project

import os
from datetime import datetime
import platform 

def main():
    print(f"Hello {os.getlogin()}! You are running {platform.system()} on {datetime.now()}")
    pass

if __name__ == "__main__":
    main()

