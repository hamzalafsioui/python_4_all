"""
Mini-Project: Common Interest Finder

This project simulates a social networking feature that finds 
common interests between two users and suggests new ones.
"""

# 1_ User Interest Profiles
user1_interests = {"Coding", "Reading", "Gaming", "Hiking", "Music"}
user2_interests = {"Gaming", "Movies", "Music", "Cooking", "Photography"}

print("=" * 40)
print("     SOCIAL CONNECT: INTEREST FINDER")
print("=" * 40)

# 2_ Find Common Interests (Intersection)
common = user1_interests & user2_interests
print(f"You both like: {', '.join(common)}")

# 3_ Suggest New Interests (Difference)
# What does User 2 like that User 1 doesn't know yet?
suggestions_for_user1 = user2_interests - user1_interests
print(f"Suggestions for User 1: {', '.join(suggestions_for_user1)}")

# 4_ Total Community Interests (Union)
all_interests = user1_interests | user2_interests
print(f"Total Unique Interests: {len(all_interests)}")

# 5_ Exclusive Interests (Symmetric Difference)
# Things that only one of them likes
exclusive = user1_interests ^ user2_interests
print(f"\nUnique to each user: {len(exclusive)} interests")

print("=" * 40)
