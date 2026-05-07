"""
Mini-Project: Simple Interest Calculator

Formula: Interest = (Principal * Rate * Time) / 100
Total Amount = Principal + Interest
"""

# 1. Define variables
principal = 5000  # Initial amount
rate = 5.5        # Annual interest rate in %
time = 3          # Time in years

# 2. Calculate Interest
interest = (principal * rate * time) / 100

# 3. Calculate Total
total_amount = principal + interest

# 4. Print the results
print("=" * 30)
print("   SAVINGS CALCULATOR")
print("=" * 30)
print(f"Principal:    ${principal}")
print(f"Rate:         {rate}%")
print(f"Time:         {time} years")
print("-" * 30)
print(f"Interest:     ${interest}")
print(f"Total Amount: ${total_amount}")
print("=" * 30)
