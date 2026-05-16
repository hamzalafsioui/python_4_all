"""
EXERCISES: The Flask Explorer

EXERCISE 1: The Info Route
1. Create a route '/info'.
2. Return a JSON object with: {"name": "[Your Name]", "language": "Python"}.

EXERCISE 2: The Multiplier
1. Create a route '/multiply/<int:num>'.
2. It should take an integer from the URL.
3. Return: {"original": num, "squared": num * num}.

EXERCISE 3: Secret Header
1. Create a route '/secret'.
2. Use 'request.headers' to check if a header named 'X-Secret-Key' exists.
3. If it exists, return {"message": "Access Granted"}.
4. If not, return {"message": "Access Denied"}, 403.

To Run: python exercises.py
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# TODO: Implement the exercises below

@app.get("/info")
def info():
    return {"name": "Hamza", "language": "Python"}

@app.get("/multiply/<int:num>")
def multiply(num: int):
    return {"original": num, "squared": num * num}

@app.get("/secret")
def secret():
    if "X-Secret-Key" in request.headers:
        return {"message": "Access Granted"}
    else:
        return {"message": "Access Denied"}, 403

if __name__ == "__main__":
    app.run(debug=True)
