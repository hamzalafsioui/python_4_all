"""
EXERCISES: The Bug Hunter

EXERCISE 1: String Reverser
1. Write a function 'reverse_string(s)' that returns the reversed string.
2. Create a test class 'TestStringReverser'.
3. Write 3 tests:
   - A normal string ("hello" -> "olleh").
   - An empty string ("" -> "").
   - A single character ("a" -> "a").

EXERCISE 2: List Average
1. Write a function 'calculate_average(numbers)' that returns the mean.
2. Create a test class 'TestListAverage'.
3. Write tests for:
   - A normal list of integers.
   - A list with one number.
   - An empty list (should it return 0 or raise an error? You decide and test it!).

EXERCISE 3: User Validator
1. Write a function 'is_adult(age)' that returns True if age >= 18.
2. Create tests for:
   - Age 20 (True).
   - Age 17 (False).
   - Age 18 (True - the boundary case!).
"""

import unittest

# TODO: Implement the functions and tests below

def reverse_string(s):
    return s[::-1]

class TestStringReverser(unittest.TestCase):
    def test_normal_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")
    
    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers) 

class TestListAverage(unittest.TestCase):
    def test_normal_list(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)
    
    def test_single_number(self):
        self.assertEqual(calculate_average([1]), 1)
    
    def test_empty_list(self):
        self.assertEqual(calculate_average([]), 0)

def is_adult(age):
    return age >= 18

class TestUserValidator(unittest.TestCase):
    def test_age_20(self):
        self.assertTrue(is_adult(20))
    
    def test_age_17(self):
        self.assertFalse(is_adult(17))
    
    def test_age_18(self):
        self.assertTrue(is_adult(18))

if __name__ == "__main__":
    unittest.main()
