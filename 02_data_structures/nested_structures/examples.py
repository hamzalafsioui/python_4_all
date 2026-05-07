"""
Examples: Data Structures - Nested Structures
This script demonstrates how to navigate and modify complex data.
"""

# ================== (1) Navigating a Matrix =======================
# A 3x3 Grid
grid = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
    ["C1", "C2", "C3"]
]

print(f"Center element: {grid[1][1]}") # Row index 1, Col index 1

print("-" * 20)

# ================== (2) Complex User Data (JSON style) =======================
social_profile = {
    "username": "hamza_dev",
    "followers": 1500,
    "settings": {
        "theme": "dark",
        "notifications": {
            "email": True,
            "sms": False
        }
    },
    "recent_posts": ["Hello World", "Learning Python", "Nested Data is cool"]
}

# Accessing deeply nested keys
email_pref = social_profile["settings"]["notifications"]["email"]
print(f"Email Notifications: {email_pref}")

# Accessing an item in a list inside a dictionary
latest_post = social_profile["recent_posts"][0]
print(f"Latest Post: {latest_post}")

print("-" * 20)

# ================== (3) Modifying Nested Data =======================
social_profile["settings"]["theme"] = "light"
social_profile["recent_posts"].append("Just updated my theme!")

print(f"Updated Theme: {social_profile['settings']['theme']}")
print(f"Post Count: {len(social_profile['recent_posts'])}")

print("-" * 20)

# ================== (4) Iterating through Nested Lists =======================
classroom = [
    ["Ali", "Aya"],
    ["Hamza", "Zakaria"],
    ["Naim", "Omar"]
]

print("Seating Chart:")
for row_idx, row in enumerate(classroom):
    print(f"Row {row_idx}: {', '.join(row)}")
