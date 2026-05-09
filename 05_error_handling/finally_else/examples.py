# Examples: Else and Finally

def divide(a, b):
    print(f"\n--- Dividing {a} by {b} ---")
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Can't divide by zero!")
    else:
        print(f"Success! Result is {result}")
    finally:
        print("Cleanup: This line always runs.")

divide(10, 2)
divide(10, 0)

# Real World Example: Resource Management
print("\n--- Example: File Handling ---")
file_name = "test.txt"
try:
    # Create the file first for the example
    with open(file_name, "w") as f:
        f.write("Hello Python!")
    
    f = open(file_name, "r")
    print("File opened.")
    # Imagine something goes wrong here
    # x = 1 / 0 
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Content: {f.read()}")
finally:
    if 'f' in locals():
        f.close()
        print("File closed via finally.")
