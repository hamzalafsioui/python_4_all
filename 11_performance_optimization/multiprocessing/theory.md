# Multiprocessing: Breaking the Speed Limit

Python is naturally a "single-threaded" language because of something called the **GIL (Global Interpreter Lock)**. This means standard Python code can only use one CPU core at a time, even if your computer has 8 or 16 cores!

To truly unlock your computer's power for heavy math or data processing, you need the `multiprocessing` module.

---

## 1. CPU-Bound vs. I/O-Bound
Before using multiprocessing, you must know what kind of problem you have:
- **CPU-Bound**: Heavy math, data processing, image manipulation. Your CPU is working at 100%. **Use Multiprocessing.**
- **I/O-Bound**: Downloading files, waiting for a database. Your CPU is resting while waiting for the network. **Do NOT use Multiprocessing** (We use Threading or Async for this, which we'll cover next).

---

## 2. The Global Interpreter Lock (GIL)
The GIL is a lock that protects Python objects, preventing multiple threads from executing Python bytecodes at once.
- `multiprocessing` bypasses the GIL by creating entirely new Python processes. Each process has its own memory space and its own GIL.
- This allows true parallel execution on multiple CPU cores.

---

## 3. `Process` vs `Pool`
There are two main ways to use multiprocessing:

### `Process` (Manual Control)
Good for starting a few distinct background tasks.
```python
from multiprocessing import Process

def my_task():
    print("Working...")

p = Process(target=my_task)
p.start() # Starts the process
p.join()  # Waits for the process to finish
```

### `Pool` (Data Parallelism)
Good when you have a massive list of data and want to split the work across all your CPU cores automatically.
```python
from multiprocessing import Pool

def square(n):
    return n * n

# Uses all available CPU cores by default
with Pool() as pool:
    results = pool.map(square, [1, 2, 3, 4, 5])
```

---

## 4. The Windows Rule: `if __name__ == "__main__":`
Because of how Windows handles processes, **any script that uses multiprocessing MUST wrap the execution code in an `if __name__ == "__main__":` block.** If you don't do this, your script will crash and spawn infinite processes!

---

## 5. Best Practices
1. **Process Creation is Slow**: Starting a new process takes time and memory. Don't use multiprocessing for fast tasks; it will actually make your code slower! Only use it for tasks taking several seconds or minutes.
2. **Avoid Shared State**: Because processes have separate memory, they don't share variables easily. Rely on passing data in (arguments) and getting data out (returns).
