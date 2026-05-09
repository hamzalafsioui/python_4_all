"""
EXERCISES: The Cleanup Master

Task:
1. Write a function `safe_write(filename, content)`:
   - Try to open the file in write mode.
   - Write the content.
   - Use an `else` block to print "Write successful!".
   - Use a `finally` block to print "Finished attempting write operation."
2. Call the function with a valid filename.
3. Call it with an invalid filename (e.g., a path that doesn't exist or a protected folder) to see how finally still runs.
"""

# TODO: Implement the safe_write function

def safe_write(filename, content):
    try:
        with open(filename, 'w') as f:
            f.write(content)
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("Write successful!")
    finally:
        print("Finished attempting write operation.")




