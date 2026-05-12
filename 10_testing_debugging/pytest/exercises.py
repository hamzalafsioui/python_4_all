"""
EXERCISES: The Pytest Pro

EXERCISE 1: The Palindrome Checker
1. Write a function 'is_palindrome(s)' (True if string reads same forward/backward).
2. Write a pytest that checks:
   - "radar" -> True
   - "python" -> False
   - "" -> True

EXERCISE 2: Fixture Fun
1. Write a function 'sum_list(numbers)'.
2. Create a fixture 'my_list' that returns [10, 20, 30].
3. Write a test that uses 'my_list' to verify 'sum_list' returns 60.

EXERCISE 3: The Power Table
1. Write a function 'power(base, exp)'.
2. Use '@pytest.mark.parametrize' to test:
   - (2, 3) -> 8
   - (5, 0) -> 1
   - (10, -1) -> 0.1
"""

import pytest

# TODO: Implement the functions and tests below
# Note: To run, use command: pytest exercises.py or 'python -m pytest 10_testing_debugging/pytest/exercises.py'

def is_palindrome(s):
    return s == s[::-1]

def sum_list(numbers):
    return sum(numbers)

def power(base, exp):
    return base ** exp

# Test Palindrome
def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("python") == False
    assert is_palindrome("") == True

# Test Sum List
def test_sum_list():
    assert sum_list([10, 20, 30]) == 60

# Test Power
@pytest.mark.parametrize("base, exp, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (10, -1, 0.1)
])
def test_power(base, exp, expected):
    assert power(base, exp) == expected

