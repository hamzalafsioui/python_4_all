"""
EXERCISES: The Multi-Handler

Task:
1. Create a dictionary with some keys and values.
2. Ask the user for a key and a number.
3. Try to get the value from the dictionary and divide it by the number.
4. Handle the following specifically:
   - Key doesn't exist.
   - Value isn't a number.
   - Number is zero.
   - User inputs something that isn't a number for the divisor.
"""

# TODO: Implement the multi-handler exercise

def divide_dict_value():
    data = {"a": 10, "b": "20"}
    
    try:
        key = input("Enter a key (a or b): ")
        divisor = input("Enter a divisor: ")
        
        value = data[key]
        result = data[key] / int(divisor)
        print(f"Result: {result:.2f}")
        
    except KeyError:
        print("Error: Key not found in dictionary!")
    except ValueError:
        print("Error: Invalid input!")
    except ZeroDivisionError:
        print("Error: Division by zero!")

divide_dict_value()
