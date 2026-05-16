# Examples: Building a Micro-Service with Flask

# .venv\Scripts\activate
# pip install flask
# flask run

from flask import Flask, jsonify, request

app = Flask(__name__)

# --- 1. Basic Route ---
@app.route("/")
def index():
    return "<h1>Welcome to the Flask API!</h1><p>Visit /api/hello to see JSON.</p>"

# --- 2. Returning JSON ---
@app.get("/api/hello")
def hello():
    # Flask automatically converts dicts to JSON in modern versions (v2.0+)
    return {"message": "Hello from Flask", "version": "3.x"}

# --- 3. Dynamic Routes (Variable Parts) ---
# Access at: http://127.0.0.1:5000/user/hamza
@app.get("/user/<name>")
def get_user(name):
    return {"user_detected": name, "status": "active"}

# --- 4. Handling POST Requests ---
@app.post("/api/echo")
def echo_data():
    # Get JSON data from the request body
    data = request.json
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
        
    return jsonify({
        "you_sent": data,
        "server_received_at": "now"
    })

if __name__ == "__main__":
    # debug=True enables auto-reloading
    app.run(debug=True, port=5000)
