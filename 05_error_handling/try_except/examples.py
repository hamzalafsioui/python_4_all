# Examples: Basic Error Handling

# 1_ Handling ZeroDivisionError
print("--- Example 1: Division ---")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Handled a division by zero!")

# 2_ Handling ValueError
print("\n--- Example 2: Type Conversion ---")
try:
    number = int("NotANumber")
except ValueError:
    print("Error: Handled an invalid integer conversion!")

# 3_ Handling IndexError
print("\n--- Example 3: List Index ---")
my_list = [1, 2, 3]
try:
    print(my_list[10])
except IndexError:
    print(f"Error: Index 10 is out of range for list of length {len(my_list)}!")
