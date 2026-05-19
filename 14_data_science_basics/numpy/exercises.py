"""
EXERCISES: The Array Wizard

EXERCISE 1: The Matrix Builder
1. Create a 1D NumPy array containing numbers from 10 to 19 (inclusive).
2. Reshape this array into a 2D matrix of shape (2, 5).
3. Print the shape, the number of dimensions, and the matrix itself.

EXERCISE 2: Statistical Aggregations
1. Create a 1D array of 20 random integers between 1 and 100.
   (Hint: use np.random.randint(1, 101, 20))
2. Calculate and print:
   - The maximum value.
   - The minimum value.
   - The mean (average).
   - The index of the maximum value (Hint: np.argmax()).

EXERCISE 3: Temperature Converter
1. Create an array of daily high temperatures in Fahrenheit:
   temps_f = [72.5, 68.0, 81.2, 90.5, 78.8, 65.3, 70.0]
2. Convert this list to a NumPy array.
3. Convert all temperatures to Celsius using the formula: C = (F - 32) * 5/9.
   (Do this in a single vectorized step!)
4. Print the resulting Celsius array rounded to 1 decimal place (Hint: np.round()).
"""

import numpy as np

# TODO: Implement the exercises above

def exercise1():
    arr = np.arange(10, 20)
    arr = arr.reshape(2, 5)
    print(arr.shape)
    print(arr.ndim)
    print(arr)

def exercise2():
    arr = np.random.randint(1, 101, 20)
    print(arr)
    print(arr.max())
    print(arr.min())
    print(arr.mean())
    print(np.where(arr == arr.max()))
    print(arr.argmax())

def exercise3():
    temps_f = [72.5, 68.0, 81.2, 90.5, 78.8, 65.3, 70.0]
    arr = np.array(temps_f)
    arr = (arr - 32) * 5/9
    print(arr)
    print(np.round(arr, 1))

if __name__ == "__main__":
    exercise1()
    print("\n")
    exercise2()
    print("\n")
    exercise3()
