"""
EXERCISES: The API Master

EXERCISE 1: Dynamic Path Parameters
1. Write a function 'get_todo(todo_id)'.
2. It should fetch the todo with that ID from "https://jsonplaceholder.typicode.com/todos/[id]".
3. Print the title and whether it is completed.

EXERCISE 2: Filtering with Query Params
1. Use the URL "https://jsonplaceholder.typicode.com/comments".
2. Write a function 'get_comments_for_post(post_id)'.
3. Use query parameters to fetch only comments belonging to that post.
4. Print how many comments were found.

EXERCISE 3: The Header Inspector
1. Make a GET request to "https://httpbin.org/headers".
2. This API returns a list of all headers YOUR computer sent.
3. Print the 'User-Agent' (this tells the server what browser/library you are using).
"""

import requests

# TODO: Implement the exercises below

def get_todo(todo_id):

    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/" + str(todo_id)
    )

    todo = response.json()

    print("Title:", todo["title"])
    print("Completed:", todo["completed"])



def get_comments_for_post(post_id):

    response = requests.get(
        "https://jsonplaceholder.typicode.com/comments",
        params={"postId": post_id}
    )

    comments = response.json()

    print("Comments found:", len(comments))


def get_headers():

    response = requests.get("https://httpbin.org/headers")

    headers = response.json()["headers"]

    print("User-Agent:", headers["User-Agent"])



if __name__ == "__main__":

    get_todo(5)
    get_comments_for_post(1)
    get_headers()

    
