# Examples: Interacting with the OS and Interpreter

import os
import sys

# 1_ OS: Exploring your system
def os_demo():
    print("--- OS Module Demo ---")
    print(f"Current Directory: {os.getcwd()}")
    print(f"OS Name: {os.name}") # 'nt' for Windows, 'posix' for Mac/Linux
    
    # List files in the current folder
    files = os.listdir(".")
    print(f"Files found: {len(files)}")
    
    # Check for an environment variable
    user = os.environ.get("USERNAME") or os.environ.get("USER")
    print(f"Current System User: {user}")

# 2_ SYS: Exploring the interpreter
def sys_demo():
    print("\n--- SYS Module Demo ---")
    print(f"Python Version: {sys.version}")
    print(f"Platform: {sys.platform}")
    
    # Command line arguments
    print(f"Arguments passed: {sys.argv}")
    if len(sys.argv) > 1:
        print(f"First argument: {sys.argv[1]}")
    else:
        print("No arguments passed. Try running: python examples.py hello 123")

# 3_ Path Management
def path_demo():
    print("\n--- OS Path Demo ---")
    # Building a path safely
    new_path = os.path.join(os.getcwd(), "test_folder", "data.txt")
    print(f"Target Path: {new_path}")
    
    print(f"Does it exist? {os.path.exists(new_path)}")

# --- Usage ---

if __name__ == "__main__":
    os_demo()
    sys_demo()
    path_demo()
