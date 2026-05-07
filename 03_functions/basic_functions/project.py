"""
Mini-Project: Modular Tip Calculator

This project refactors the simple tip calculator from earlier into 
reusable functions.
"""

def print_header():
    """Prints a styled header for the app."""
    print("=" * 30)
    print("      TIP CALCULATOR 2.0")
    print("=" * 30)

def calculate_and_print_bill(amount, tip_percentage):
    """Calculates the tip and total bill, then prints the result."""
    tip_amount = amount * (tip_percentage / 100)
    total_bill = amount + tip_amount
    
    print(f"Subtotal:  ${amount:>8.2f}")
    print(f"Tip ({tip_percentage}%): ${tip_amount:>8.2f}")
    print("-" * 30)
    print(f"TOTAL:     ${total_bill:>8.2f}")
    print("=" * 30)

# --- Simulation ---
print_header()

# Scenario 1: Quick lunch
print("\nScenario: Quick Lunch")
calculate_and_print_bill(25.50, 15)

# Scenario 2: Dinner with friends
print("\nScenario: Dinner with Friends")
calculate_and_print_bill(120.00, 20)
