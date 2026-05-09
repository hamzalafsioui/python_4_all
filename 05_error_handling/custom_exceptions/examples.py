# Examples: Custom Exceptions

# 1_ Define the Exception
class AgeLimitError(Exception):
    """Raised when a user is too young for a service."""
    def __init__(self, age, minimum, message="Access Denied: Too young."):
        self.age = age
        self.minimum = minimum
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} (Your age: {self.age}, Required: {self.minimum})"

# 2_ Function that raises the error
def enter_club(age):
    MIN_AGE = 18
    if age < MIN_AGE:
        raise AgeLimitError(age, MIN_AGE)
    print("Welcome to the club!")

# 3_ Handling the error
print("--- Testing Age Limit ---")
for test_age in [21, 15]:
    try:
        enter_club(test_age)
    except AgeLimitError as e:
        print(f"Caught Custom Error: {e}")
