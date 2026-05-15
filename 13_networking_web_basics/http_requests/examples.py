# Examples: Fetching and Posting Data

import requests
import json


# --- 1. GET Request ---
def get_demo():
    print("--- GET Request Demo ---")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        response = requests.get(url, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            print(f"Success! Status Code: {response.status_code}")
            
            # Convert JSON response to Python Dictionary
            data = response.json()
            print(f"Title: {data['title']}")
            print(f"User ID: {data['userId']}")
        else:
            print(f"Failed with status: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")

# --- 2. POST Request ---
def post_demo():
    print("\n--- POST Request Demo ---")
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Data to send (Python Dictionary)
    new_post = {
        "title": "Learning Python Networking",
        "body": "This is a post created via the requests library!",
        "userId": 1
    }
    
    try:
        # requests.post automatically converts the dict to JSON if you use 'json='
        response = requests.post(url, json=new_post, timeout=10)
        
        if response.status_code == 201: # 201 means "Created"
            print("Post created successfully!")
            print(f"Response: {response.json()}")
        else:
            print(f"Failed: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")

if __name__ == "__main__":
    # Note: Run 'pip install requests' first!
    get_demo()
    post_demo()
