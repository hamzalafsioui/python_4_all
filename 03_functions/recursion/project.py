"""
Mini-Project: Directory Size Calculator

This project simulates a file system using nested dictionaries and uses
recursion to calculate the total size of each "folder".
"""

# 1_ Simulated file system (nested dictionary)
# Files have integer values (size in KB). Folders have dict values.
file_system = {
    "root": {
        "documents": {
            "report.pdf": 250,
            "notes.txt": 10,
            "archives": {
                "old_data.zip": 1200,
                "backup.zip": 800
            }
        },
        "images": {
            "photo1.jpg": 150,
            "photo2.jpg": 200,
            "wallpaper.png": 500
        },
        "config.ini": 5
    }
}

def get_size(node):
    """
    Recursively calculates the total size of a file system node.
    - Base Case: if the node is an integer, it's a file -> return its size.
    - Recursive Case: it's a folder -> sum up all its children's sizes.
    """
    # Base Case: it's a file (int value)
    if isinstance(node, int):
        return node
    
    # Recursive Case: it's a folder (dict)
    total = 0
    for item in node.values():
        total += get_size(item) # Recurse into each child
    return total

def print_tree(node, name="root", indent=0):
    """Recursively prints the file system as a tree."""
    prefix = "    " * indent
    if isinstance(node, int):
        print(f"{prefix}-- {name} ({node} KB)")
    else:
        size = get_size(node)
        print(f"{prefix}[{name}] ({size} KB total)")
        for child_name, child_node in node.items():
            print_tree(child_node, child_name, indent + 1) # Recurse

# --- Simulation ---
print("=" * 40)
print("       FILE SYSTEM ANALYZER")
print("=" * 40)

print_tree(file_system)

print("-" * 40)
total_size = get_size(file_system)
print(f"Total Size: {total_size} KB")
print("=" * 40)
