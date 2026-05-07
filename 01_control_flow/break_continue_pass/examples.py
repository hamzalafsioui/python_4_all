"""
Examples: Control Flow - Break, Continue, Pass
"""

# ================== (1) Break (Search Example) =======================
names = ["Hamza", "Ali", "Omar", "Lil"]
target = "Omar"

print(f"Searching for {target}...")
for name in names:
    if name == target:
        print("Found it!")
        break # No need to keep looking
    print(f"Checking {name}...")

print("-" * 20)

# ================== (2) Continue (Filter Example) =======================
# Only print odd numbers
print("Odd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue # Skip even numbers
    print(i)

print("-" * 20)

# ================== (3) Pass (Placeholder Example) =======================
def unfinished_logic():
    # We know we need a function here, but haven't written it yet.
    # Without 'pass', this would cause a Syntax Error.
    pass 

print("Pass example executed without error.")

print("-" * 20)

# ================== (4) Break in While Loop =======================
# Infinite loop with manual break
while True:
    # Simulate some event
    condition_met = True 
    if condition_met:
        print("Breaking out of infinite loop!")
        break
