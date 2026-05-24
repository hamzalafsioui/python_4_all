# Recursion

Recursion is a programming technique where a function calls itself to solve a problem. It is often used for tasks that can be broken down into smaller, identical sub-tasks (like traversing a folder structure or calculating mathematical sequences).

---

## 1. The Two Pillars of Recursion
Every recursive function MUST have two parts to work correctly:

1.  **Base Case**: The condition that stops the recursion. Without this, the function will call itself forever and cause a `RecursionError` (Stack Overflow).
2.  **Recursive Case**: The part where the function calls itself with a slightly modified (usually smaller) version of the original problem.

---

## 2. Example: Factorial
The factorial of a number `n` (written as `n!`) is the product of all positive integers less than or equal to `n`.
Example: `5! = 5 * 4 * 3 * 2 * 1 = 120`.

```python
def factorial(n):
    # 1. Base Case
    if n == 1:
        return 1
    
    # 2. Recursive Case
    return n * factorial(n - 1)
```

---

## 3. How it Works (The Call Stack)
When a function calls itself, the computer "pauses" the current function and adds a new one on top of the "stack". Once the base case is reached, the results "bubble back up" through the stack until the final answer is calculated.

---

## 4. Pros and Cons
- **Pros**: Can make complex logic (like tree traversal) much cleaner and easier to read.
- **Cons**: Can be less memory-efficient than loops for simple tasks, as each call consumes space on the stack.

---

# Updated content with Resources
> [!CAUTION]
> Always ensure your base case is reachable! If you define `factorial(-1)`, the recursion will never stop and the program will crash.

---

## Resources

- **Official Python Recursion Documentation** – https://docs.python.org/3/reference/compound_stmts.html#recursive-functions
- **Real Python: Recursion in Python** – https://realpython.com/python-recursion/
- **Corey Schafer: Recursion (YouTube)** – https://www.youtube.com/watch?v=Mv9NEXX1VHc
- **GeeksforGeeks: Recursion in Python** – https://www.geeksforgeeks.org/recursion-in-python/
- **Fluent Python (Book) – Chapter on Recursion** – https://www.oreilly.com/library/view/fluent-python/9781491946237/

