"""
EXERCISES: The Code Detective

EXERCISE 1: The Factorial Flaw
1. The function below should calculate the factorial of a number (5! = 120).
2. It has a bug. Place a 'breakpoint()' inside the loop.
3. Run the script and use 'p i' and 'p result' to see what's happening.
4. Fix the bug.

def factorial(n):
    result = 0 # Hint: What should the starting number for multiplication be?
    for i in range(1, n + 1):
        result *= i
    return result

EXERCISE 2: Nested Data Inspection
1. You are receiving a "complex" user dictionary.
2. The code crashes when trying to access the 'zip_code'.
3. Use 'breakpoint()' to inspect the 'user' object and find where the data is missing.

def get_user_zip(user):
    # breakpoint()
    return user["address"]["zip_code"]

dummy_user = {
    "name": "Hamza",
    "info": {
        "address": {
            "city": "London"
            # Zip code is missing!
        }
    }
}
"""

# TODO: Implement the exercises below

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def get_user_zip(user):
    # breakpoint()
    return user["info"]["address"]["zip_code"]

dummy_user = {
    "name": "Hamza",
    "info": {
        "address": {
            "city": "London",
            # Zip code is missing!
            # "zip_code": "12334"
        }
    }
}

if __name__ == "__main__":
    print(factorial(5))
    print(get_user_zip(dummy_user))
    pass
