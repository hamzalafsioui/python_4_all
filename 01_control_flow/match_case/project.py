"""
Mini-Project: CLI Command Router

A simple program that simulates a command-line interface router using 
structural pattern matching.
"""

def handle_command(command_parts):
    match command_parts:
        case ["help"]:
            print("Available commands: help, load <file>, save <file>, exit")
        
        case ["load", filename]:
            print(f"Loading data from {filename}...")
            
        case ["save", filename]:
            print(f"Saving data to {filename}...")
            
        case ["exit"]:
            print("Goodbye!")
            return False
            
        case _:
            print("Error: Unknown command or wrong arguments.")
    
    return True

# Simulation
print("Welcome to the Match-Case Router!")
commands = [
    ["help"],
    ["load", "data.csv"],
    ["save", "backup.db"],
    ["delete", "secret.txt"], # Should trigger unknown
    ["exit"]
]

for cmd in commands:
    print(f"\n> {' '.join(cmd)}")
    if not handle_command(cmd):
        break
