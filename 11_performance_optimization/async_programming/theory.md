# Async Programming: The Event Loop

In the previous lesson, we learned that **Threading** uses multiple "threads" to handle I/O-bound tasks. **Asynchronous Programming** (or `asyncio`) is a more modern, lightweight way to achieve the same thing using a single thread and an **Event Loop**.

---

## 1. The Core Concept: The Waiter
Imagine a waiter in a restaurant:
- **Synchronous**: The waiter takes an order, goes to the kitchen, and **stands there** waiting for the food. No one else gets served.
- **Asynchronous**: The waiter takes an order, gives it to the kitchen, and **goes to serve other tables** while the food is cooking.

---

## 2. Key Keywords
- **`async def`**: Defines a **Coroutine**. Coroutines don't run immediately when called; they return a coroutine object.
- **`await`**: Tells Python: "Pause this function here, go do other work, and come back when this task is finished."
- **`asyncio.run()`**: The entry point to start the Event Loop.
- **`asyncio.gather()`**: Runs multiple coroutines concurrently and waits for all of them to finish.

---

## 3. Async vs Threading
| Feature | Threading | Async (asyncio) |
| :--- | :--- | :--- |
| **Management** | Managed by the Operating System | Managed by Python (Event Loop) |
| **Memory** | High (each thread uses ~8MB) | Very Low (single thread) |
| **Complexity** | Risk of Race Conditions | Easier to reason about (single thread) |
| **Usage** | Best for legacy code or specific I/O | Best for modern high-scale web apps |

---

## 4. Why use Async?
Modern web servers (like FastAPI) and networking libraries use `asyncio` because it can handle **thousands** of concurrent connections on a single CPU core with very little memory.

---

## 5. Basic Syntax
```python
import asyncio

async def say_hello():
    print("Hello...")
    await asyncio.sleep(1) # Non-blocking sleep
    print("...World!")

asyncio.run(say_hello())
```

---

## 6. Best Practices
1. **Don't Block the Loop**: Never use `time.sleep()` inside an `async def` function. It will freeze the entire program. Always use `await asyncio.sleep()`.
2. **Await Everything**: If a function is defined with `async def`, you must `await` it.
3. **Use Gather for Speed**: If you have 10 tasks, don't `await` them one by one. Use `asyncio.gather(*tasks)` to run them all at once.

## Resources

- **Official Python asyncio Documentation** – https://docs.python.org/3/library/asyncio.html
- **Real Python: Async IO in Python: A Complete Walkthrough** – https://realpython.com/async-io-python/
- **Asyncio Explained (YouTube Video)** – https://www.youtube.com/watch?v=Xbl7XjFYsOU
- **FastAPI Documentation (Async/Await)** – https://fastapi.tiangolo.com/async/
- **Using Asyncio in Python (Book)** – https://www.oreilly.com/library/view/using-asyncio-in/9781492075325/
