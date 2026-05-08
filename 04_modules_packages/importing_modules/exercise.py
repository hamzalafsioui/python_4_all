"""
EXERCISE: Import Ninja

Task:
1. Import only the 'pi' constant from the 'math' module.
2. Import the 'randint' function from the 'random' module and rename it to 'get_random'.
3. Import the 'platform' module as 'plt'.
4. Print the current OS platform using 'plt.system()'.
5. Generate a random number between 1 and 10 using 'get_random'.
6. Calculate the area of a circle with radius 5 using your imported 'pi'.
"""

# TODO: Add your imports here

from math import pi
from random import randint as get_random
import platform as plt 

def main():
    # TODO: Implement the logic here
    print(f"current OS: {plt.system()}")
    print(f"random number between 1 and 10: {get_random(1, 10)}")
    print(f"area of circle with radius 5: {pi * 5 ** 2}")
    pass

if __name__ == "__main__":
    main()
