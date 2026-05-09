"""
PROJECT: Simple Task Manager

Goal: Create a CLI tool to manage a 'todo.txt' file.

Requirements:
1. The script should show a menu: 
   1. View Tasks
   2. Add Task
   3. Clear All Tasks
   q. Quit
2. View Tasks: Read 'todo.txt' and print all tasks with numbers (e.g., "1. Buy Milk").
3. Add Task: Ask the user for a task and append it to 'todo.txt'.
4. Clear All: Overwrite 'todo.txt' with an empty string or simply delete the file contents.

Bonus: Handle the FileNotFoundError if 'todo.txt' doesn't exist when the user tries to view tasks.
"""

# TODO: Implement the Task Manager
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TODO_PATH = os.path.join(BASE_DIR, "todo.txt")

def main():
    while True:
        print("\n--- Simple Task Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Clear All Tasks")
        print("q. Quit")
        choice = input("Enter your choice: ").strip().lower()
        match choice:
            case "1":
                view_tasks()
                pass
            case "2":
                add_task()
                pass
            case "3":
                clear_tasks()
                pass
            case "q":
                print("Exiting the application...")
                break

def view_tasks():
    try:
        with open(TODO_PATH, "r") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("No tasks found.")

def add_task():
    task = input("Enter your task: ")
    with open(TODO_PATH, "a") as f:
        f.write(task + "\n")

def clear_tasks():
    with open(TODO_PATH, "w") as f:
        f.write("")


if __name__ == "__main__":
    main()
