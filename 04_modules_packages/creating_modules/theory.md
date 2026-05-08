# Creating Your Own Modules

A module is just a Python file. By creating your own, you can reuse code across different projects and keep your scripts clean.

---

## 1. Creating a Module
To create a module, just save your Python code in a `.py` file. 

**Example: `my_math.py`**
```python
def add(a, b):
    return a + b

PI = 3.14
```

To use it in `main.py`:
```python
import my_math
print(my_math.add(5, 5))
```

---

## 2. The `if __name__ == "__main__":` Block
When you import a module, Python executes all the code in it. If you have print statements or tests in your module, they will run every time someone imports it.

To prevent this, use the `if __name__ == "__main__":` block.
- `__name__` is a special variable in Python.
- If the file is run directly: `__name__ == "__main__"`
- If the file is imported: `__name__ == "module_name"`

```python
def my_func():
    print("Doing something...")

if __name__ == "__main__":
    # This only runs when you execute this file directly
    print("Testing my_func:")
    my_func()
```

---

## 3. Module Search Path
When you say `import my_module`, Python looks in:
1. The current directory.
2. The standard library folders.
3. Folders listed in your `PYTHONPATH` environment variable.

---

> [!IMPORTANT]
> Never name your module the same as a standard library module. For example, naming your module `random.py` will break any code that tries to use the real `random` module!
