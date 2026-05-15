"""
EXERCISES: The API Architect

EXERCISE 1: The Personal Greeter
1. Create a route '/greet/{name}'.
2. It should return a JSON message: {"message": "Hello [name], welcome to FastAPI!"}.

EXERCISE 2: The Math API
1. Create a route '/sum' that takes two query parameters: 'a' and 'b' (both integers).
2. It should return the sum: {"result": a + b}.
3. Test it in the /docs UI.

EXERCISE 3: User Registration
1. Create a Pydantic model 'User' with 'username' (str) and 'email' (str).
2. Create a POST route '/register' that accepts this User model.
3. Return the user info back with a "success" status.

To Run: uvicorn exercises:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# TODO: Implement the exercises above

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello {name}, welcome to FastAPI!"}

@app.get("/sum")
def sum(a: int, b: int):
    return {"result": a + b}

@app.post('/register')
class User(BaseModel):
    username: str
    email: str
def register(user: User):
    return {"message": "User created", "data": user}


# python -m uvicorn 13_networking_web_basics.custom_api_fastapi.exercises:app --reload