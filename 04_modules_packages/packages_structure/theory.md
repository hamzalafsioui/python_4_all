# 📂 Packages Structure

When your project grows, having 50 modules in one folder becomes messy. **Packages** allow you to group related modules into directories.

---

## 1. What makes a folder a Package?
Historically, a directory **must** contain a file named `__init__.py` for Python to treat it as a package. 
- In modern Python (3.3+), this is technically optional (called "Namespace Packages"), but it is still highly recommended to include `__init__.py` for clarity and compatibility.

---

## 2. Importing from a Package
Use the dot `.` notation to navigate the folder structure.

**Example Structure:**
```text
my_project/
├── main.py
└── my_package/
    ├── __init__.py
    ├── database.py
    └── auth.py
```

**Importing:**
```python
from my_package import auth
import my_package.database
```

---

## 3. The `__init__.py` file
This file runs whenever the package is imported. You can use it to:
- Perform package-level initialization.
- Export specific functions to the package level so they are easier to import.

Example `__init__.py`:
```python
from .auth import login  # Allows "import my_package; my_package.login()"
```

---

## 4. Absolute vs. Relative Imports
- **Absolute**: `from my_package.auth import login` (Always safer).
- **Relative**: `from .auth import login` (Used inside a package to refer to neighbors).

---

> [!TIP]
> Keep your package structure shallow. Deeply nested packages (e.g., `a.b.c.d.e.f.module`) are hard to navigate and maintain.

---

## Resources

- **Official Python Packaging Documentation** – https://packaging.python.org/tutorials/packaging-projects/
- **Real Python: Python Packages** – https://realpython.com/python-modules-packages/
- **Corey Schafer: Python Packages (YouTube)** – https://www.youtube.com/watch?v=0sOvCWFmrtA
- **GeeksforGeeks: Python Packages** – https://www.geeksforgeeks.org/python-packages/
- **Fluent Python (Book) – Chapter on Packages** – https://www.oreilly.com/library/view/fluent-python/9781491946237/
