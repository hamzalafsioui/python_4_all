# Examples: Parameters and Authentication

import requests

# 1_ Path Parameters
# Fetches a specific item by its ID in the URL path
def get_user_by_id(user_id):
    print(f"--- Fetching User {user_id} ---")
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json()['name'])
    else:
        print("User not found.")

# 2_ Query Parameters
# Filters the results using a dictionary passed to 'params'
def get_posts_by_user(user_id):
    print(f"\n--- Fetching Posts for User {user_id} ---")
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # query params: ?userId=1
    query_params = {"userId": user_id}
    
    response = requests.get(url, params=query_params)
    posts = response.json()
    print(f"Found {len(posts)} posts.")
    for post in posts[:3]: # Show first 3
        print(f"- {post['title']}")

# 3_ Authentication Headers (Simulator)
def authenticated_request_demo():
    print("\n--- Auth Header Demo ---")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    # In a real API, you would put your secret key here
    headers = {
        "Authorization": "Bearer my_secret_token_123",
        "Accept": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    print(f"Status: {response.status_code}")

if __name__ == "__main__":
    get_user_by_id(5)
    get_posts_by_user(1)
    authenticated_request_demo()
