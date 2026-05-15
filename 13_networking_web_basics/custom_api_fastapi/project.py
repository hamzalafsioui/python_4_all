"""
PROJECT: The Task Manager API

Goal: Build a real API to manage a Todo list (in-memory).

Requirements:

1. Data Setup:
   - Create an in-memory list: 'tasks = []'
   - Create a Pydantic model 'Task': 'id' (int), 'title' (str), 'is_completed' (bool, default=False).

2. The Routes:
   - 'GET /tasks': Returns the full list of tasks.
   - 'POST /tasks': Adds a new task to the list.
   - 'GET /tasks/{task_id}': Finds and returns a specific task by ID.
   - 'DELETE /tasks/{task_id}': Removes a task from the list.

3. Testing:
   - Start the server: uvicorn project:app --reload
   - Open 'http://127.0.0.1:8000/docs'.
   - Use the POST tool to add 3 tasks.
   - Use the GET tool to list them.
   - Delete one and verify it's gone.

Real-World Logic:
- This is a "Stateful API." Even though we aren't using a database yet, the 'tasks' list stays alive as long as the server is running. This is the first step toward building full-scale backend systems for mobile and web apps.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# TODO: Implement the Task Manager API

tasks = []

class Task(BaseModel):
    id: int
    title: str
    is_completed: bool = False

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

# python -m uvicorn 13_networking_web_basics.custom_api_fastapi.project:app --reload
