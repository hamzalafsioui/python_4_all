# Reading Files in Python

Reading files allows your program to process data stored on the computer's hard drive. Python makes this very easy with the built-in `open()` function.

---

## 1. The `with` Statement (Recommended)
The best way to open a file is using the `with` statement. 
- **Why?** It automatically closes the file for you, even if an error occurs. This prevents memory leaks and file corruption.

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here
```

---

## 2. Opening Modes
The second argument of `open()` is the **mode**. For reading, we use:
- `"r"`: Read (default). Fails if the file doesn't exist.
- `"rb"`: Read Binary (used for images, PDFs, etc.).

---

## 3. Ways to Read Content
1. `file.read()`: Reads the **entire** file into a single string.
2. `file.readline()`: Reads just **one line** at a time.
3. `file.readlines()`: Reads all lines and returns them as a **list of strings**.
4. **Looping**: You can iterate over the file object directly (most memory-efficient for large files).

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip()) # strip() removes the newline character
```

---

## 4. The File Pointer
When you read from a file, Python keeps track of where you are. If you call `read()` twice, the second call will return an empty string because the "pointer" is already at the end of the file.
- Use `file.seek(0)` to move the pointer back to the beginning.

---

> [!IMPORTANT]
> Always check if a file exists before trying to read it, or wrap your code in a `try/except FileNotFoundError` block to prevent crashes!
