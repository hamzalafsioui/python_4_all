"""
EXERCISES: The Decorator Challenge

EXERCISE 1: The Simple Logger
1. Create a decorator '@logger' that prints "Executing [function_name]..." every time the function is called.
2. Test it on a function 'add(a, b)'.

EXERCISE 2: The Repeater
1. Create a decorator that takes an argument 'n' and runs the decorated function 'n' times.
   Hint: This requires a "decorator factory" (a function that returns a decorator).
2. Test it on a function 'shout()' that prints "Hello!".

EXERCISE 3: The Delay Decorator
1. Create a decorator '@delay' that waits for 2 seconds before executing the function.
2. Test it on a function 'slow_print(text)'.
"""

from functools import wraps
import time

# TODO: Implement the exercises below

# 1_ The Simple Logger
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

def repeater(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

def delay(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(2)
        return func(*args, **kwargs)
    return wrapper

if __name__ == "__main__":

   print("\nPART 1: The Simple Logger") 
   @logger
   def add(a, b):
      return a + b
    
   print(f"add(1,2) ----> {add(1, 2)}")
    
   print("\nPART 2: The Repeater")
   @repeater(3)
   def shout():   
      print("Hello!")
    
   shout()
    
   print("\nPART 3: The Delay Decorator")
   @delay
   def slow_print(text):
      print(text)
    
   slow_print("Hello!")   
