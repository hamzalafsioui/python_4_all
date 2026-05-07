"""
Exercises: Control Flow - For Loops
"""

# Exercise 1: Count Even Numbers
# Use a for loop and range() to print all even numbers between 1 and 20 (inclusive).

# Your code here:

for number in range(1,21):
    if number % 2 == 0:
        print(number)


# ----------------------------------------------------------------

# Exercise 2: List Transformation
# Given a list of numbers, create a new list that contains 
# the square of each number.
numbers = [1, 2, 3, 4, 5]
squares = []

# Your code here:

for number in numbers:
    squares.append(number**2)
print(squares)

# ----------------------------------------------------------------

# Exercise 3: Vowel Counter
# Ask the user for a word and count how many vowels (a, e, i, o, u) are in it.
word = "Python Mastery"
vowel_count = 0

# Your code here:

for w in word:
    match w:
        case 'a' | 'e' | 'i' | 'o' | 'u':
            vowel_count += 1
print(vowel_count)

# ----------------------------------------------------------------

# Exercise 4: Pattern Printing
# Use nested for loops to print the following pattern:
# *
# **
# ***
# ****
# *****

# Your code here:

for x in range(1,6):
    print(x * '*')

# use nested loops

for x in range(1,6):
    for y in range(x):
        print('*', end='')
    print()

# ----------------------------------------------------------------
