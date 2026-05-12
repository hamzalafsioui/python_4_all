# Examples: Specialized Containers in Action

from collections import namedtuple, Counter, defaultdict, deque

# 1_ NamedTuple: Self-Documenting Data
def namedtuple_demo():
    print("--- NamedTuple Demo ---")
    User = namedtuple("User", ["id", "name", "email"])
    u1 = User(1, "Hamza", "hamza@example.com")
    
    print(f"User Name: {u1.name}")
    print(f"Full Tuple: {u1}")

# 2_ Counter: Frequency Tracking
def counter_demo():
    print("\n--- Counter Demo ---")
    text = "apple banana apple cherry banana apple"
    words = text.split()
    
    word_counts = Counter(words)
    print(f"Word Counts: {dict(word_counts)}")
    print(f"Most common: {word_counts.most_common(1)}")

# 3_ DefaultDict: Grouping Items
def defaultdict_demo():
    print("\n--- DefaultDict Demo ---")
    data = [("fruit", "apple"), ("veg", "carrot"), ("fruit", "banana")]
    
    # Group items by category
    category_map = defaultdict(list)
    for category, item in data:
        category_map[category].append(item)
        
    print(f"Grouped Data: {dict(category_map)}")

# 4_ Deque: The Last N Items
def deque_demo():
    print("\n--- Deque Demo ---")
    # Keep only the last 3 items
    recent_actions = deque(maxlen=3)
    
    actions = ["Login", "View Page", "Click Button", "Logout"]
    for action in actions:
        recent_actions.append(action)
        print(f"History: {list(recent_actions)}")

# --- Usage ---

if __name__ == "__main__":
    namedtuple_demo()
    counter_demo()
    defaultdict_demo()
    deque_demo()
