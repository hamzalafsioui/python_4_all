"""
PROJECT: The Database Transaction Simulator

Goal: Simulate a database transaction where you either commit all changes or rollback if an error occurs.

Requirements:
1. Variables `db_connected = False` and `transaction_active = False`.
2. Function `start_transaction()`: Sets both to True.
3. Function `execute_query(query)`: 
   - If query contains "DROP", raise a `RuntimeError`.
   - Else, print "Executing: [query]".
4. Main Logic:
   - Try to start a transaction and execute a list of queries.
   - If an error occurs, print "ROLLBACK: Undoing changes".
   - If no error occurs, print "COMMIT: Changes saved".
   - Use `finally` to set `db_connected` and `transaction_active` back to False and print "Connection closed".
"""

# TODO: Implement the project


db_connected = False
transaction_active = False


def start_transaction():
    global db_connected, transaction_active

    db_connected = True
    transaction_active = True

    print("Transaction started")


def execute_query(query):
    if "DROP" in query.upper():
        raise RuntimeError("Dangerous query detected!")

    print(f"Executing: {query}")


# List of queries
queries = [
    "SELECT * FROM users",
    "UPDATE users SET name='Hamza' WHERE id=1",
    "DROP TABLE users"   # This will trigger rollback
]

try:
    start_transaction()

    for query in queries:
        execute_query(query)

    print("COMMIT: Changes saved")

except RuntimeError as error:
    print(f"Error: {error}")
    print("ROLLBACK: Undoing changes")

finally:
    db_connected = False
    transaction_active = False

    print("Connection closed")