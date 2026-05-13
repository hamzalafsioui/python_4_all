# Threading: Mastering the Waiting Game

In the last lesson, we learned that **Multiprocessing** is for **CPU-Bound** tasks (heavy math). But what if your program is slow because it's waiting for a website to load, or a file to download? 

That is an **I/O-Bound** task, and the perfect tool for it is **Threading**.

---

## 1. Why Threading over Multiprocessing?
- **Lightweight**: Threads use much less memory than processes. You can easily spawn 100 threads, but spawning 100 processes might crash your computer.
- **Shared Memory**: Threads live inside the same Python process, meaning they can easily share variables and state.

---

## 2. The GIL (Again!)
Remember the Global Interpreter Lock (GIL)? It prevents multiple threads from executing Python code at the exact same time. 
**So why does Threading work?**
Because when a thread says, "I'm waiting for this website to respond," the GIL is **released**. Python immediately switches to another thread to do work while the first thread waits. 

---

## 3. How to use Threading

### The Modern Way: `ThreadPoolExecutor`
Introduced in the `concurrent.futures` module, this is the easiest and safest way to manage threads.

```python
import concurrent.futures
import time

def download(url):
    time.sleep(1) # Simulate waiting for the internet
    return f"Downloaded {url}"

urls = ["site1.com", "site2.com", "site3.com"]

# This takes 1 second total, not 3 seconds!
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(download, urls)
```

---

## 4. Race Conditions
Because threads share memory, if two threads try to modify the same variable at the exact same time, you get a "Race Condition" (corrupted data).
- **Rule of Thumb**: Try to avoid having threads modify the exact same variable. Have them *return* data instead, or use a `threading.Lock()` if you absolutely must modify shared state.

---

## 5. Summary
- **Math/Data Processing** -> CPU-Bound -> Use `multiprocessing`.
- **Downloading/Web Scraping/Databases** -> I/O-Bound -> Use `threading`.
