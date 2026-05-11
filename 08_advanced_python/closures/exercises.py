"""
EXERCISES: The Memory Game

EXERCISE 1: The Tag Maker
1. Write a closure factory 'make_tag(tag)'.
2. It should return a function that wraps text in that tag.
   Example:
   p_tag = make_tag("p")
   print(p_tag("Hello")) # Output: <p>Hello</p>

EXERCISE 2: The Running Average
1. Write a closure 'make_averager()'.
2. It should remember all numbers passed to it and return the current average.
   Example:
   avg = make_averager()
   avg(10) # 10.0
   avg(20) # 15.0

EXERCISE 3: Authorization Check
1. Write a closure 'make_auth(password)'.
2. It should return a function that takes a 'guess'.
3. The returned function returns True if the guess is correct, False otherwise.
"""

# TODO: Implement the exercises below

def make_tag(tag: str):
    def tagger(text: str):
        return f"<{tag}>{text}</{tag}>"
    return tagger

def make_averager():
    total = 0
    count = 0
    def averager(num: int):
        nonlocal total, count
        total += num
        count += 1
        return total / count
    return averager

def make_auth(password: str):
    def authenticator(guess: str):
        return guess == password
    return authenticator


if __name__ == "__main__":

    print("--- Tag Maker ---")
    p_tag = make_tag("p")
    print(p_tag("Hello"))

    print("\n--- Running Average ---")
    avg = make_averager()
    print(avg(10))
    print(avg(20))

    print("\n--- Authorization Check ---")
    auth = make_auth("secret")
    print(auth("secret"))
    print(auth("wrong"))
