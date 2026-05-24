# Flask: The Micro-Framework

Before FastAPI existed, **Flask** was the king of Python web development. It is a "micro-framework," meaning it is very lightweight and gives you complete control over how you build your application.

---

## 1. Why Flask?
- **Simplicity**: You can build a web server in just 5 lines of code.
- **Flexibility**: Flask doesn't force you to use specific tools (like a specific database). You choose your own "stack."
- **Maturity**: Thousands of huge companies (like Pinterest and LinkedIn) still use Flask because it's battle-tested.

---

## 2. Installation
```bash
pip install flask
```

---

## 3. Basic Components

### The App Instance
```python
from flask import Flask
app = Flask(__name__)
```

### Routes and Methods
In Flask, you specify the methods in the decorator.
```python
@app.route("/", methods=["GET"])
def home():
    return "Hello, World!"
```

### JSON Responses
Unlike FastAPI, Flask doesn't automatically convert dictionaries to JSON. You usually use the `jsonify` function.
```python
from flask import jsonify

@app.route("/api")
def api():
    return jsonify({"status": "ok"})
```

---

## 4. Accessing Data
To see what the user sent you, use the `request` object:
- **`request.args`**: For query parameters (`?name=hamza`).
- **`request.json`**: For JSON data sent in a POST request.

---

## 5. How to Run
By default, Flask runs on port **5000**.
```bash
python main.py
```
*(Note: To enable auto-reloading, you usually add `app.run(debug=True)` at the bottom of your script).*

---

## 6. Flask vs. FastAPI
| Feature | Flask | FastAPI |
| :--- | :--- | :--- |
| **Speed** | Fast | Blazing Fast (Async) |
| **Validation** | Manual | Automatic (Pydantic) |
| **Docs** | Manual | Automatic (/docs) |
| **Feel** | Flexible/Traditional | Modern/Strict |

## Resources

- **Official Flask Documentation** – https://flask.palletsprojects.com/
- **Flask Mega‑Tutorial (Miguel Grinberg)** – https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
- **Flask vs FastAPI Comparison** – https://testdriven.io/blog/fastapi-vs-flask/
- **Deploying Flask with Docker** – https://testdriven.io/blog/dockerizing-flask/
- **Flask Testing Guide** – https://flask.palletsprojects.com/en/2.3.x/testing/
