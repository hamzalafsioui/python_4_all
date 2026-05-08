# Examples: Multiple Exceptions

def process_data(data, key, divisor):
    print(f"\n--- Processing: data={data}, key={key}, divisor={divisor} ---")
    try:
        val = data[key]
        num = int(val)
        result = num / divisor
        print(f"Result: {result}")
    except KeyError:
        print("Error: Key not found in dictionary!")
    except ValueError:
        print(f"Error: Could not convert '{val}' to an integer!")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# Test Cases
my_dict = {"a": "10", "b": "hello"}

process_data(my_dict, "a", 2)    # Success
process_data(my_dict, "c", 2)    # KeyError
process_data(my_dict, "b", 2)    # ValueError
process_data(my_dict, "a", 0)    # ZeroDivisionError
