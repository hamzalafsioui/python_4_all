# Importing Modules

In Python, a module is just a file containing code. To use code from one file in another, we **import** it.

---

## 1. The `import` Statement
The simplest way to bring in a module is the `import` keyword. This brings the entire module into your current script's namespace.

```python
import math
print(math.sqrt(16)) # Access using module_name.function
```

---

## 2. The `from ... import` Statement
If you only need specific parts of a module, you can import them directly. This makes your code cleaner but can sometimes lead to name conflicts.

```python
from math import pi, sqrt
print(pi)   # No need for math.pi
print(sqrt(16))
```

---

## 3. The `as` Keyword (Aliasing)
You can rename a module or function during import. This is very common in data science (e.g., `import numpy as np`).

```python
import datetime as dt
print(dt.datetime.now())
```

---

## 4. The `*` Wildcard (Avoid This!)
You can import *everything* from a module using `*`. 
**Warning**: This is generally considered bad practice because it clutters your namespace and makes it hard to tell where functions came from.

```python
from random import *
print(randint(1, 10)) # Where did randint come from? Hard to tell in large files.
```

---

> [!TIP]
> Always place your imports at the **top** of your Python files. This follows the PEP 8 style guide and makes dependencies clear immediately.

---

## Resources

- **Official Python Import System Documentation** – https://docs.python.org/3/reference/import.html
- **Real Python: Importing Modules in Python** – https://realpython.com/python-modules-packages/
- **Corey Schafer: Python Modules and Packages (YouTube)** – https://www.youtube.com/watch?v=CqvZ3vGoGs0
- **GeeksforGeeks: Python Modules** – https://www.geeksforgeeks.org/python-modules/
- **Fluent Python (Book) – Chapter on Modules** – https://www.oreilly.com/library/view/fluent-python/9781491946237/
