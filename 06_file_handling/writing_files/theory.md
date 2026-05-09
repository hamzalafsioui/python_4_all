# Writing Files in Python

Writing to files allows you to save data permanently. Python provides several modes for writing, depending on whether you want to create a new file, overwrite an existing one, or add to it.

---

## 1. Writing Modes
When you use `open(filename, mode)`, the `mode` parameter determines how Python handles the file:

- **`"w"` (Write)**: Opens a file for writing. 
  - **Warning**: If the file already exists, it will be **completely overwritten** (erased). If it doesn't exist, it creates a new one.
- **`"a"` (Append)**: Opens a file for appending. 
  - New data is added to the **end** of the file. Existing content is preserved.
- **`"x"` (Exclusive Creation)**: Creates a new file. 
  - Fails (raises an error) if the file already exists.
- **`"w+"`**: Opens for both reading and writing (overwrites existing).

---

## 2. Writing Methods
1. `file.write(string)`: Writes a string to the file. It does **not** add a newline (`\n`) automatically.
2. `file.writelines(list)`: Writes a list of strings to the file. Again, it doesn't add newlines automatically.

```python
with open("output.txt", "w") as f:
    f.write("Hello World\n")
    f.write("This is a second line.")
```

---

## 3. Buffering
When you call `write()`, Python might not save the data to the disk immediately (for performance reasons). It stores it in a "buffer" first.
- Data is physically saved when you **close** the file (which the `with` statement does automatically).
- You can manually force a save using `file.flush()`.

---

> [!CAUTION]
> Be extremely careful with the `"w"` mode. One mistake can permanently delete all the data in a file! Always double-check your filenames before running your script.
