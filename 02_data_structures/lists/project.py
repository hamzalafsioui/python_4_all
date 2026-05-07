"""
Mini-Project: Simple Task Manager

In this project, you will build a simple command-line task manager using lists.
We will simulate adding, removing, and viewing tasks.
"""

# ============= (1) Initialize Task List ===========
tasks = ["Learn Python", "Build a project", "Go for a run"]

# ============= (2) Add a New Task ===========
new_task = "Read a book"
tasks.append(new_task)
print(f"Added: '{new_task}'")

# ============= (3) Mark a Task as Done (Remove it) ===========
# Let's say we finished the first task.
completed_task = tasks.pop(0)
print(f"Completed: '{completed_task}'")

# ============= (4) Update a Task ===========
# Change "Build a project" to "Build a Web App"
tasks[0] = "Build a Web App"

# ============= (5) Display the Final List ===========
print("\n" + "=" * 30)
print("       CURRENT TASKS")
print("=" * 30)

# We'll use a simple loop (even though we haven't officially covered them in this folder,
# it's a good preview!)
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")

print("-" * 30)
print(f"Total tasks remaining: {len(tasks)}")
print("=" * 30)

# ============= (6) Clear all tasks ===========
tasks.clear()
print("All tasks cleared!")
