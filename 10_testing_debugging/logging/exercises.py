"""
EXERCISES: The Log Master

EXERCISE 1: The Login Monitor
1. Create a function 'login(username, password)'.
2. Use 'logging.info' for successful logins.
3. Use 'logging.warning' for failed logins.
4. Set the logging level to INFO and run it.

EXERCISE 2: The Error Tracker
1. Create a function 'process_data(data_list)'.
2. If the list is empty, log an 'ERROR' and return.
3. If the list contains a non-integer, log a 'WARNING' and skip that item.
4. Configure the logger to save to a file named 'data_errors.log'.

EXERCISE 3: Custom Formatter
1. Configure a logger that uses the following format:
   "TIME: [LEVEL] -> MESSAGE"
   (Hint: Use asctime, levelname, and message keys).
"""

import logging

# TODO: Implement the exercises below

# excercise 1

def login(username, password):
    logging.info(f"User {username} has logged in.")
    if password == "1234":
        logging.info(f"User {username} has logged in.")
    else:
        logging.warning(f"User {username} has failed to log in.")

# excercise 2

def process_data(data_list):
    if len(data_list) == 0:
        logging.error("The list is empty.")
    for item in data_list:
        if not isinstance(item, int):
            logging.warning(f"The item {item} is not an integer.")

# excercise 3

def divide(a, b):
    try:
        result = a / b
        logging.info(f"Result of {a} / {b} = {result}")
    except ZeroDivisionError:
        logging.error("Cannot divide by zero")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s: [%(levelname)s] -> %(message)s"
    )
    login("Hamza", "1234")
    process_data([1, 2, "s", 4, 5])
    divide(10, 0)
