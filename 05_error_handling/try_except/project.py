"""
PROJECT: Reliable Data Parser

Goal: Create a function that safely extracts an integer from a list at a given index.

Requirements:
1. Function `get_int_from_list(data_list, index)`:
   - Try to access the list at `index`.
   - Try to convert the value to an integer.
   - Return the integer if successful.
   - Return `None` and print a specific error message if it's an IndexError or ValueError.

Example:
data = ["10", "abc", "20"]
get_int_from_list(data, 0) -> 10
get_int_from_list(data, 1) -> None (prints "Value 'abc' is not an integer")
get_int_from_list(data, 5) -> None (prints "Index 5 is out of bounds")
"""

# TODO: Implement the project

def get_int_from_list(data_list, index):
    try:
        value = data_list[index]
        return int(value)
    except IndexError:
        print(f"Error: Index {index} is out of bounds for list of length {len(data_list)}!")
        return None
    except ValueError:
        print(f"Error: Value '{data_list[index]}' is not an integer!")
        return None

print(get_int_from_list(["10", "abc", "20"], 0))
print(get_int_from_list(["10", "abc", "20"], 1))
print(get_int_from_list(["10", "abc", "20"], 5))