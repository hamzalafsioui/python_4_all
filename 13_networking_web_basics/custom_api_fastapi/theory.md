# FastAPI: Building Professional APIs

Up until now, we've been *consuming* APIs from other people. In this lesson, we will learn how to **build our own**. **FastAPI** is currently the most popular modern web framework for Python because it is incredibly fast, easy to write, and automatically generates documentation for you.

---

## 1. Why FastAPI?
- **Speed**: It's as fast as NodeJS and Go (thanks to `starlette` and `pydantic`).
- **Auto-Documentation**: Every time you build a route, FastAPI builds a website for you to test it (at `/docs`).
- **Type Safety**: It uses Python type hints to validate data automatically.
- **Async Support**: It works perfectly with `async` and `await`.

---

## 2. Installation
To run a FastAPI app, you need the framework and a server called `uvicorn`.
```bash
pip install fastapi uvicorn
```

---

## 3. Basic Components

### The App Instance
This is the heart of your API.
```python
from fastapi import FastAPI
app = FastAPI()
```

### Path Operations (Routes)
Decorators tell FastAPI which URL and which HTTP Method to handle.
```python
@app.get("/")
def home():
    return {"message": "Welcome to my API"}
```

### Automatic Data Validation (Pydantic)
FastAPI uses `Pydantic` to ensure the data sent by the user matches what you expect.
```python
from pydantic import BaseModel

class User(BaseModel):
    username: str
    age: int
```

---

## 4. How to Run the Server
You don't run the script with `python script.py`. You use the `uvicorn` command:
```bash
uvicorn main:app --reload
```
- `main`: The name of your file (e.g., `main.py`).
- `app`: The name of the `FastAPI()` object inside that file.
- `--reload`: Automatically restarts the server whenever you save your code.

---

## 5. Testing your API
Once the server is running, visit:
- **`http://127.0.0.1:8000`**: To see your API's output.
- **`http://127.0.0.1:8000/docs`**: To see the Interactive Swagger documentation.

---

## 6. Best Practices
1. **Use Type Hints**: Always define your parameters as `id: int` or `name: str`. FastAPI uses this to return a 422 error if the user sends the wrong data type.
2. **Pydantic for POST**: Always use Pydantic models for the "Body" of a POST request.
3. **Async when possible**: If your API is doing I/O (database, network), use `async def` for better performance.
