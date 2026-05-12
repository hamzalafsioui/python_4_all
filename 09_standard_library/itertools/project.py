"""
PROJECT: Brute-Force Password Simulator

Goal: Use 'itertools.product' to simulate how a brute-force password cracker works.

Requirements:

1. Setup:
   - Target Password: "abc"
   - Possible Characters: "abcdefghijklmnopqrstuvwxyz"

2. The Cracker Logic:
   - Use 'itertools.product(chars, repeat=n)' to generate all possible combinations of a specific length 'n'.
   - Start with length 1, then 2, then 3.
   - For each combination, join the characters into a string.
   - Check if the generated string matches the target password.
   - If it matches, print "Password found: [password]" and stop.

Real-World Logic:
- This demonstrates why short passwords are weak. 
- You'll see that as the length increases, the number of combinations grows exponentially. This is the "Combinatorial Explosion."
"""

# TODO: Implement the Password Cracker
import itertools
import time

def crack_password(target, chars):
    print(f"Attempting to crack: {target}")
    start_time = time.time()
    
    # Try lengths 1 to 4
    for length in range(1, 5):
        print(f"Trying length: {length}...")
        # itertools.product generates all possible combinations with replacement
        for guess in itertools.product(chars, repeat=length):
            guess_str = "".join(guess)
            if guess_str == target:
                end_time = time.time()
                print(f"SUCCESS! Password found: {guess_str}")
                print(f"Time taken: {end_time - start_time:.4f}s")
                return True
    return False

if __name__ == "__main__":
    target = "abbc"
    possible_chars = "abcdefghijklmnopqrstuvwxyz"
    crack_password(target, possible_chars)
