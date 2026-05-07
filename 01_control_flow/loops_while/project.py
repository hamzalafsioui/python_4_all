"""
Mini-Project: The Number Guessing Game

In this project, the computer picks a random number, and you have to 
guess it. The program will give you hints if your guess is too high 
or too low.
"""

import random

# 1_ Setup
secret_number = random.randint(1, 20)
guess = 0
attempts = 0

print("=" * 30)
print("   NUMBER GUESSING GAME")
print("=" * 30)
print("I'm thinking of a number between 1 and 20.")

# 2_ Main Loop
# In a real game, you would use: guess = int(input("Enter guess: "))
# Here, we'll simulate a few guesses.

simulated_guesses = [10, 15, 12, 13] # Let's say secret is 13

for sim_guess in simulated_guesses:
    attempts += 1
    guess = sim_guess
    print(f"\nAttempt {attempts}: Guessing {guess}...")
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"BINGO!  You found it in {attempts} attempts.")
        break # Exit the loop immediately

print("\n" + "=" * 30)
print("      GAME OVER")
print("=" * 30)
