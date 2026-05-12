"""
PROJECT: The Broken Payroll System

Goal: Find and fix the bugs in a salary calculation script.

Bugs to Find:
1. The overtime calculation is incorrect.
2. The tax deduction is being applied twice.
3. One employee's name is being skipped.

Instructions:
1. Run the script. Look at the incorrect output.
2. Place 'breakpoint()' at the start of the 'calculate_payroll' function.
3. Use 'n' to step through the loop for each employee.
4. Use 'p' to check the intermediate calculations.
5. Fix the code until the output matches the "Expected" values.

Expected Output:
- Hamza: $4000
- Alice: $5500
- Bob: $3000
"""

def calculate_payroll(employees):
    results = {}
    for emp in employees:
        # breakpoint()
        name = emp["name"]
        hours = emp["hours"]
        rate = emp["rate"]
        
        # Logic Error 1: Overtime (anything over 40 hours should be rate * 1.5)
        if hours > 40:
            overtime_hours = hours - 40
            total = (40 * rate) + (overtime_hours * rate) # BUG: Should be rate * 1.5
        else:
            total = hours * rate
            
        # Logic Error 2: Tax (Apply 10% tax)
        tax = total * 0.1
        total = total - tax
        total = total - (total * 0.1) # BUG: Deducting tax twice!
        
        results[name] = total
    return results

employees_data = [
    {"name": "Hamza", "hours": 40, "rate": 100},
    {"name": "Ali", "hours": 50, "rate": 100},
    {"name": "Morad", "hours": 35, "rate": 100}
]

if __name__ == "__main__":
    payroll = calculate_payroll(employees_data)
    for name, salary in payroll.items():
        print(f"{name}: ${salary}")
