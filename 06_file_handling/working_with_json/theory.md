# Working with JSON in Python

**JSON** (JavaScript Object Notation) is the most popular format for exchanging data on the web. It looks almost identical to Python dictionaries and lists, which makes it very easy to work with.

---

## 1. The `json` Module
Python comes with a built-in `json` module. You must import it first:
```python
import json
```

---

## 2. Key Terms: Serialization & Deserialization
- **Serialization (Dumping)**: Converting a Python object (like a dict) into a JSON string or file.
- **Deserialization (Loading)**: Converting a JSON string or file back into a Python object.

---

## 4. The 4 Main Functions
There are four functions you need to know. The ones ending in **`s`** are for **S**trings; the others are for **F**iles.

| Function | Action | Direction |
| :--- | :--- | :--- |
| `json.dumps()` | Serialize to **String** | Python -> String |
| `json.dump()` | Serialize to **File** | Python -> File |
| `json.loads()` | Deserialize from **String** | String -> Python |
| `json.load()` | Deserialize from **File** | File -> Python |

---

## 5. Formatting (Pretty Printing)
When writing JSON to a file, it's often all on one line. You can make it human-readable using the `indent` parameter.

```python
data = {"name": "Hamza", "age": 25}
with open("user.json", "w") as f:
    json.dump(data, f, indent=4)
```

---

> [!NOTE]
> JSON keys must always be strings (wrapped in double quotes `"`), whereas Python dictionary keys can be any hashable type (like integers or tuples).

## Resources

- **Official Python json Documentation** – https://docs.python.org/3/library/json.html
- **Real Python: Working with JSON Data** – https://realpython.com/python-json/
- **Corey Schafer: JSON in Python (YouTube)** – https://www.youtube.com/watch?v=9N6a-VLBa2I
- **JSON.org Specification** – https://www.json.org/json-en.html
- **Python for Everybody – Chapter on JSON** – https://www.py4e.com/book

