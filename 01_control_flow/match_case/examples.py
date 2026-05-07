"""
Examples: Control Flow - Match Case
Note: Requires Python 3.10+
"""

# ================== (1) Command Processing =======================
command = "QUIT"

match command.lower():
    case "start":
        print("System starting...")
    case "stop" | "quit" | "exit":
        print("Shutting down safely.")
    case "restart":
        print("Rebooting...")
    case _:
        print("Unknown command.")

print("-" * 20)

# ================== (2) Pattern Matching with Data =======================
# Matching list structure
user_action = ["move", "forward", 10]

match user_action:
    case ["stop"]:
        print("Stopping immediately.")
    case ["move", direction, steps]:
        print(f"Moving {direction} by {steps} steps.")
    case _:
        print("Invalid action format.")

print("-" * 20)

# ================== (3) Match with Guards =======================
age = 25

match age:
    case n if n < 13:
        print("You are a child.")
    case n if 13 <= n < 20:
        print("You are a teenager.")
    case n if n >= 20:
        print("You are an adult.")
