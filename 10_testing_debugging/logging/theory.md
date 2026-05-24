# Logging: The Black Box of Your Software

In professional software, we almost never use `print()`. If a program crashes on a user's computer, we can't see their screen. Instead, we use **Logging** to write a history of events to a file. This file acts like an airplane's "Black Box," allowing us to see exactly what happened leading up to a crash.

---

## 1. Why Use Logging instead of Print?
- **Persistence**: Logs go to a file that survives after the program stops.
- **Severity Levels**: You can categorize messages (e.g., "Just an update" vs "CRITICAL FAILURE").
- **Formatting**: Logs automatically include timestamps, line numbers, and filenames.
- **Control**: You can turn off "Debug" logs in production with one single line of code.

---

## 2. The 5 Standard Levels
Logging uses a hierarchy. If you set the level to `INFO`, you will see `INFO`, `WARNING`, `ERROR`, and `CRITICAL`, but NOT `DEBUG`.

1. **DEBUG**: Detailed info for diagnosing problems.
2. **INFO**: Confirmation that things are working as expected.
3. **WARNING**: An indication that something unexpected happened (e.g., "Disk space low").
4. **ERROR**: A more serious problem (e.g., "Could not save file").
5. **CRITICAL**: A serious error indicating the program itself may be unable to continue.

---

## 3. Basic Setup
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log"
)

logging.info("Application started")
logging.error("Failed to connect to database")
```

---

## 4. Best Practices
1. **Never Log Secrets**: Don't log passwords, API keys, or credit card numbers.
2. **Use Timestamps**: Always include `%(asctime)s` in your format.
3. **Log Exceptions**: Use `logging.exception("message")` inside an `except` block to automatically capture the full traceback.
4. **Separate Files**: Log "system events" to one file and "user actions" to another if the app is large.

## Resources

- **Official Python logging Documentation** – https://docs.python.org/3/library/logging.html
- **Python Logging Tutorial (Real Python)** – https://realpython.com/python-logging/
- **Python Logging Basics (YouTube)** – https://www.youtube.com/watch?v=-ARI4CzFsWA
- **Logging in Python: A Developer's Guide** – https://www.loggly.com/ultimate-guide/python-logging-basics/
- **Good Logging Practice in Python** – https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
