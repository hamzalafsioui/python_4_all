# Comments and Style (PEP 8)

Writing code that works is only half the job. Writing code that **humans can read** is the other half.

---

## 1. Comments
Comments are notes for humans. Python ignores them during execution.

### Single-line Comments
Use `#` for short notes.
```python
# Calculate the area
area = length * width
```

### Multi-line Comments (Docstrings)
Use triple quotes `"""` for documentation at the top of files or functions.
```python
"""
This script calculates the orbit of a planet.
Version: 1.0
"""
```

---

## 2. The "Why" vs. the "What"
- **Bad Comment**: `x = x + 1 # Add 1 to x` (The code already says this!)
- **Good Comment**: `x = x + 1 # Account for the buffer item` (Explains the reasoning).

---

## 3. PEP 8 Style Guide
PEP 8 is the official style guide for Python code.

### Key Rules:
- **Indentation**: Use 4 spaces per level.
- **Variable Names**: Use `snake_case` (e.g., `user_score`, not `UserScore`).
- **Line Length**: Limit lines to 79 characters.
- **Whitespaces**: Use spaces around operators (`x = 5`, not `x=5`).

---

## 4. Descriptive Naming
Avoid names like `a`, `b`, `c`. Use names that describe the data.

- **Bad**: `d = 86400`
- **Good**: `seconds_in_a_day = 86400`

---

> [!TIP]
> "Code is read much more often than it is written." — Guido van Rossum (Creator of Python)
