# Examples: Using Your Own Modules

import utils

# 1_ Accessing functions
print(f"Greeting: {utils.greet('Hamza')}")

# 2_ Accessing constants
print(f"Module Version: {utils.VERSION}")

# 3_ Using specific functions
from utils import power
print(f"2 to the power of 10: {power(2, 10)}")

# 4_ Checking if the __main__ block worked
# Notice that the print statements inside utils.py's __main__ block 
# did NOT appear in this output!
