"""
Examples: Control Flow - While Loops
"""

# ================== (1) Basic Counter =======================
timer = 5
print("Countdown starting...")

while timer > 0:
    print(timer)
    timer -= 1

print("Blast off! ")

print("-" * 20)

# ================== (2) User Input Loop =======================
# This simulates waiting for a specific user action
user_input = ""
while user_input.lower() != "quit":
    user_input = input("Enter a message (type 'quit' to exit): ")
    print(f"You said: {user_input}")

print("-" * 20)

# ================== (3) Data Processing =======================
# Removing items from a list until it's empty
queue = ["User1", "User2", "User3"]

while queue:
    current_user = queue.pop(0)
    print(f"Processing {current_user}...")
    print(f"Remaining in queue: {len(queue)}")

print("All users processed.")

print("-" * 20)

# ================== (4) Random Number Condition =======================
import random

target = 7
current = 0
attempts = 0

while current != target:
    current = random.randint(1, 10)
    attempts += 1
    print(f"Attempt {attempts}: Rolled a {current}")

print(f"Found {target} in {attempts} attempts!")
