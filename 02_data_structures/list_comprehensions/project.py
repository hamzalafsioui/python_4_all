"""
Mini-Project: Smart Data Cleanup Tool

This project simulates cleaning up a messy list of user-provided data 
using list comprehensions.
"""

# 1_ Raw messy data
raw_users = [
    "  ali  ", 
    "Jamal", 
    "  Hamza", 
    "Hasan_dev", 
    "Ahmed_dev", 
    "guest",
    "123"
]

print("=" * 40)
print("     SMART DATA CLEANUP")
print("=" * 40)

# 2_ Cleanup Step 1: Strip whitespace and lowercase everything
clean_stage1 = [u.strip().lower() for u in raw_users]
print(f"Stage 1 (Strip/Lower): {clean_stage1}")

# 3_ Cleanup Step 2: Remove numeric or invalid users
# For this demo, let's keep only users that don't start with a number
valid_users = [u for u in clean_stage1 if not u[0].isdigit()]
print(f"Stage 2 (Filter):      {valid_users}")

# 4_ Cleanup Step 3: Flag special users
# Users with '_dev' in their name get a "[DEV]" prefix
processed_users = [
    f"[DEV] {u.replace('_dev', '')}" if "_dev" in u else u 
    for u in valid_users
]

# 5_ Output Final Results
print("-" * 40)
print("Final Processed Users:")
for user in processed_users:
    print(f"- {user}")
print("=" * 40)
