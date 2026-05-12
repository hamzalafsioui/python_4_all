# Examples: Creating a Mini-CLI Tool

import argparse

def greet_demo():
    # 1. Initialize the Parser
    parser = argparse.ArgumentParser(description="A simple greeting CLI tool.")

    # 2. Add Arguments
    # Positional (Required)
    parser.add_argument("name", help="The name of the person to greet")
    
    # Optional with Type and Default
    parser.add_argument("-a", "--age", type=int, help="The age of the person", default=25)
    
    # Flag (True/False)
    parser.add_argument("-u", "--uppercase", action="store_true", help="Convert greeting to uppercase")

    # 3. Parse the Arguments
    args = parser.parse_args()

    # 4. Use the Data
    message = f"Hello {args.name}! You are {args.age} years old."
    
    if args.uppercase:
        print(message.upper())
    else:
        print(message)

# To test this, run:
# python examples.py Hamza --age 20 --uppercase

if __name__ == "__main__":
    # We use try/except because parse_args() exits the script on error/help
    try:
        greet_demo()
    except SystemExit:
        pass
