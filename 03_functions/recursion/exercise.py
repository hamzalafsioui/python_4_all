"""
Exercises: Functions - Recursion
"""

# Exercise 1: Power Function
# Write a recursive function 'recursive_power' that calculates 
# base^exponent without using the ** operator.
# Hint: 2^3 = 2 * 2^2 = 2 * 2 * 2^1 = 2 * 2 * 2 * 2^0
# Base Case: exponent == 0 -> return 1

# Your code here:

def recursive_power(base, exponent):
    if exponent == 0:
        return 1
    return base * recursive_power(base, exponent - 1)

print(recursive_power(2, 10))

# ----------------------------------------------------------------

# Exercise 2: Reverse a String
# Write a recursive function 'reverse_string' that reverses a string.
# Hint: "abc" reversed is "c" + reverse("ab")
# Base Case: len(string) == 0 -> return ""

# Your code here:

def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))


# ----------------------------------------------------------------

# Exercise 3: Count Occurrences
# Write a recursive function 'count_occurrences' that counts how many 
# times an item appears in a list.
# Base Case: empty list -> return 0

# Your code here:

def count_occurrences(lst,item):
    if not lst:
        return 0
    return (1 if lst[0] == item else 0) + count_occurrences(lst[1:], item)

print(count_occurrences([1, 2, 2, 3, 4, 4, 5, 1, 6], 4))


# ----------------------------------------------------------------

# Exercise 4: Nested Sum
# Write a recursive function 'nested_sum' that takes a list which may 
# contain integers or other lists, and returns the total sum.
# Example: [1, [2, 3], [4, [5]]] -> 15

# Your code here:

def nested_sum(lst):
    if not lst:
        return 0
    total = 0
    for i in lst:
        if type(i) == list:
            total += nested_sum(i)
        else:
            total += i
    return total

print(nested_sum([1, [2, 3], [4, [5]]]))
