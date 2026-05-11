# Closures: Function Memory

A **Closure** is one of the most powerful concepts in Python. It allows a function to "remember" and access variables from its outer (enclosing) scope even after the outer function has finished executing.

---

## 1. Prerequisites: Nested Functions
To have a closure, you must first have a nested function (a function inside another function).

```python
def outer():
    x = 10
    def inner():
        print(x) # Accesses x from outer
    return inner
```

---

## 2. The 3 Criteria for a Closure
For a function to be considered a closure, it must meet these three requirements:
1. We must have a **nested function**.
2. The nested function must refer to a value defined in the **enclosing scope**.
3. The enclosing function must **return** the nested function.

---

## 3. The `nonlocal` Keyword
If you want to **modify** a variable from the outer scope inside the inner function, you must use the `nonlocal` keyword. Without it, Python will think you are trying to create a new local variable.

```python
def make_counter():
    count = 0
    def counter():
        nonlocal count # Critical for modification!
        count += 1
        return count
    return counter
```

---

## 4. Why Use Closures?
1. **Data Hiding**: You can create "private" variables that can't be accessed from outside the function.
2. **Avoiding Globals**: They provide a way to store state without using messy global variables.
3. **Function Factories**: You can create specialized functions on the fly (e.g., a function that specifically multiplies by 5).

---

## 5. Best Practices
1. **Don't Overuse**: If your closure logic gets too complex, it's usually better to use a **Class**.
2. **Memory Awareness**: Since closures "remember" variables, those variables stay in memory as long as the closure exists. Be careful with large data sets.
3. **Naming**: Use descriptive names for the "factory" function and the "returned" function to avoid confusion.
