# Input and Output (I/O)

How your program talks to the user and vice versa.

---

## 1. Output with `print()`
The `print()` function is used to output data to the standard output device (screen).

```python
print("Hello World")
```

### Advanced `print()`
- **Multiple Arguments**: `print("Hamza", 25)` # Hamza 25
- **Separator**: `print("A", "B", "C", sep="-")`  # A-B-C
- **End Character**: `print("Hello", end="!")`  # No newline at the end

---

## 2. Input with `input()`
The `input()` function allows the user to enter data into the program.

```python
name = input("Enter your name: ")
```

### CRITICAL: Input is ALWAYS a String
Even if the user types a number, Python reads it as a string. You must **cast** it to the correct type.

```python
age = int(input("Enter your age: ")) # Convert string to integer
```

---

## 3. Formatting Strings (f-strings)
F-strings are the modern, recommended way to format strings in Python (introduced in Python 3.6).

```python
name = "Hamza"
score = 95
print(f"User {name} scored {score} points.")
```

---

> [!TIP]
> You can even perform math inside f-strings!
> `print(f"10 + 5 is {10 + 5}")`
