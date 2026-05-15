"""
EXERCISES: The Web Explorer

EXERCISE 1: The Status Checker
1. Write a function 'check_status(url)' that:
   - Tries to GET the URL.
   - Returns the status code.
   - Handles exceptions (returns 0 if the site is down).
2. Test it with "https://www.google.com" and "https://this-site-does-not-exist-123.com".

EXERCISE 2: User Data Fetcher
1. Use the URL: "https://jsonplaceholder.typicode.com/users".
2. Fetch the list of users.
3. Print the 'name' and 'email' of every user in the list.

EXERCISE 3: Searching for Todos
1. The URL "https://jsonplaceholder.typicode.com/todos" returns a list of tasks.
2. Fetch the list.
3. Count how many tasks are 'completed' (completed == True).
4. Print the total count.
"""

import requests
import json

# TODO: Implement the exercises below

def check_status(url):

    response = requests.get(url)

    return response.status_code

if __name__ == "__main__":
    
    # Exercise 1
    print('='*40)
    print('Exercise 1: The Status Checker')
    print('='*40)

    try:
        print(check_status("https://www.google.com"))
    except Exception as e:
        print(0)
    
    try:
        print(check_status("https://this-site-does-not-exist-123.com"))
    except Exception as e:
        print(0)

    # Exercise 2

    print('='*40)
    print('Exercise 2: User Data Fetcher')
    print('='*40)

    response = requests.get("https://jsonplaceholder.typicode.com/users")

    users = response.json()

    for user in users:

        print(user["name"], user["email"])

    # Exercise 3

    print('='*40)
    print('Exercise 3: Searching for Todos')
    print('='*40)

    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    todos = response.json()

    count = 0

    for todo in todos:

        if todo["completed"]:

            count += 1

    print(count)
