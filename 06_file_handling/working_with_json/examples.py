# Examples: JSON Serialization & Deserialization

import json
import os

# Get directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "data.json")

# 1_ Python Object to JSON String (dumps)
person = {
    "name": "Hamza",
    "is_student": False,
    "skills": ["Python", "Machine Learning", "DevOps"],
    "address": {
        "city": "Paris",
        "zip": "75001"
    }
}

json_string = json.dumps(person, indent=2)
print("--- JSON String ---")
print(json_string)

# 2_ Python Object to JSON File (dump)
print(f"\n--- Saving to {os.path.basename(JSON_FILE)} ---")
with open(JSON_FILE, "w") as f:
    json.dump(person, f, indent=4)

# 3_ JSON File back to Python Object (load)
print("\n--- Reading from File ---")
with open(JSON_FILE, "r") as f:
    data_from_file = json.load(f)
    print(f"Name: {data_from_file['name']}")
    print(f"First Skill: {data_from_file['skills'][0]}")

# 4_ JSON String to Python Object (loads)
raw_json = '{"brand": "Ford", "model": "Mustang", "year": 1964}'
car = json.loads(raw_json)
print(f"\n--- String to Dict ---")
print(f"Car Brand: {car['brand']}")
