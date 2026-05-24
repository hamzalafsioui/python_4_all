# Lambda Functions (Anonymous Functions)

A lambda function is a small, anonymous function that can take any number of arguments, but can only have **one expression**.

---

## 1. Syntax
The syntax is simple: `lambda arguments : expression`

**Standard Function:**
```python
def square(x):
    return x * x
```

**Lambda Equivalent:**
```python
square = lambda x : x * x
```

---

## 2. Why use Lambdas?
- **Conciseness**: They are great for one-line logic.
- **Throwaway Functions**: Used when you need a function for a short period, especially as an argument to another function.
- **Functional Tools**: They work perfectly with `map()`, `filter()`, and `sorted()`.

---

## 3. Using Lambdas with `filter()`
`filter()` takes a function and a list, and returns only the items that make the function `True`.

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Result: [2, 4, 6]
```

---

## 4. Using Lambdas with `map()`
`map()` applies a function to every item in a list.

```python
numbers = [1, 2, 3]
doubled = list(map(lambda x: x * 2, numbers))
# Result: [2, 4, 6]
```

---

## 5. Using Lambdas with `sorted()`
You can use lambdas to define a custom "key" for sorting complex data.

```python
users = [("Ali", 25), ("Hamza", 20), ("Zakaria", 30)]
# Sort by age (the second item in the tuple)
sorted_users = sorted(users, key=lambda user: user[1])
```

---

> [!CAUTION]
> Don't over-use lambdas! if your logic is complex or requires multiple lines, use a standard `def` function for better readability.

## Resources

- **Official Python Documentation on Lambdas** – https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
- **Real Python: How to Use Python Lambda Functions** – https://realpython.com/python-lambda/
- **Corey Schafer: Lambda Expressions Tutorial (YouTube)** – https://www.youtube.com/watch?v=25ovCm9jKfA
- **Functional Programming in Python** – https://docs.python.org/3/howto/functional.html

