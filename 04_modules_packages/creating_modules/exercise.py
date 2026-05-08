"""
EXERCISE: The String Master

1. Create a file named 'text_processor.py' in this directory.
2. Inside 'text_processor.py', create two functions:
   - reverse_string(s): returns the string backwards.
   - uppercase_string(s): returns the string in all caps.
3. In THIS file (exercise.py), import those functions and use them on a sample string.
"""

# TODO: Add your imports here

from text_processor import reverse_string, uppercase_string

def main():
    sample = "Python Modules are Awesome"
    
    # TODO: Use your text_processor functions here
    print(f"Original: {sample}")
    print(f"Reversed: {reverse_string(sample)}")
    print(f"Uppercase: {uppercase_string(sample)}")
    
if __name__ == "__main__":
    main()
