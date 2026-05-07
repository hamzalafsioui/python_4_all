"""
Mini-Project: Social Media Feed Simulator

This project demonstrates how to handle complex nested data representing 
a social media feed (User -> Posts -> Comments).
"""

# 1_ Database of users and their content
feed = [
    {
        "author": "Ali",
        "content": "Just started learning Python!",
        "stats": {"likes": 15, "shares": 2},
        "comments": [
            {"user": "Hamza", "text": "Nice work!"},
            {"user": "Aya", "text": "Good luck!"}
        ]
    },
    {
        "author": "Zakaria",
        "content": "Anyone here using VS Code?",
        "stats": {"likes": 8, "shares": 0},
        "comments": []
    }
]

def display_feed():
    print("=" * 40)
    print("       PYTHON SOCIAL FEED")
    print("=" * 40)
    
    for post in feed:
        print(f"\n  @{post['author']}")
        print(f">>> content: {post['content']}")
        print(f">>>> likes: {post['stats']['likes']}  || shares: {post['stats']['shares']}")
        
        if post['comments']:
            print(">>>>>>>>>>Comments")
            for comment in post['comments']:
                print(f">>>>>>>>>>>>>>>>>>>> @{comment['user']}: {comment['text']}")
        else:
            print("   (No comments yet)")
        print("-" * 40)

# 2_ Add a new comment to Ali's post
def add_comment(post_index, user, text):
    new_comment = {"user": user, "text": text}
    feed[post_index]["comments"].append(new_comment)
    print(f"\n[OK] Added comment by {user}.")

# --- Simulation ---
display_feed()

# Add a comment to the first post (Ali)
add_comment(0, "Naim", "I love this language!")

# Update likes on the second post
feed[1]["stats"]["likes"] += 1

display_feed()
