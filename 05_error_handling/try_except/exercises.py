"""
EXERCISES: The Crash-Proof Input

Task:
1. Write a script that asks the user for two numbers.
2. Try to divide the first number by the second.
3. Use a try-except block to handle:
   - Non-numeric input (ValueError).
   - Division by zero (ZeroDivisionError).
4. If an error occurs, print a helpful message and don't let the script crash.
"""

# TODO: Implement the crash-proof division here

def main():
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

if __name__ == "__main__":
    main()
