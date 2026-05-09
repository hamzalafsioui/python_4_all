"""
PROJECT: Advanced User Validation System

Goal: Create a registration system that uses multiple custom exceptions to validate user input.

Requirements:
1. Create three custom exceptions:
   - `UsernameTooShortError` (less than 3 chars)
   - `UsernameForbiddenError` (contains "admin" or "root")
   - `PasswordTooWeakError` (less than 8 chars or doesn't contain a digit)
2. Create a function `register_user(username, password)` that checks all these rules.
3. The function should raise the appropriate exception as soon as a rule is broken.
4. Main Logic:
   - Ask for username and password.
   - Try to register the user.
   - Catch each custom exception specifically and print a user-friendly error message.
   - Use an `else` block to print "Registration Successful!" if no errors occur.
"""

# TODO: Implement the validation system


class UsernameTooShortError(Exception):
    """Raised when username is too short."""
    def __init__(self, username, min_length=3):
        self.username = username
        self.min_length = min_length
        super().__init__(f"Username is too short. Minimum length is {min_length} characters.")

class UsernameForbiddenError(Exception):
    """Raised when username contains forbidden words."""
    def __init__(self, username, forbidden_words):
        self.username = username
        self.forbidden_words = forbidden_words
        super().__init__(f"Username contains forbidden words: {', '.join(forbidden_words)}")

class PasswordTooWeakError(Exception):
    """Raised when password is too weak."""
    def __init__(self, password, min_length=8):
        self.password = password
        self.min_length = min_length
        super().__init__(f"Password is too weak. Minimum length is {min_length} characters and must contain at least one digit.")

def register_user(username, password):
    if len(username) < 3:
        raise UsernameTooShortError(username)
    if username in ["admin", "root"]:
        raise UsernameForbiddenError(username, ["admin", "root"])
    if len(password) < 8 or not any(char.isdigit() for char in password):
        raise PasswordTooWeakError(password)
    print("Registration successful!")

# Example usage:
try:
    register_user("hamza", "12345678")
    register_user("hamza", "1234567")
    register_user("admin", "123")
    register_user("root", "12345678")
except UsernameTooShortError as e:
    print(f"Caught Custom Error: {e}")
except UsernameForbiddenError as e:
    print(f"Caught Custom Error: {e}")
except PasswordTooWeakError as e:
    print(f"Caught Custom Error: {e}")
else:
    print("All registrations successful!")

# another way to do the same thing
for username, password in [("hamza", "12345678"), ("hamza", "1234567"), ("admin", "123"), ("root", "12345678")]:
    try:
        register_user(username, password)
    except UsernameTooShortError as e:
        print(f"Caught Custom Error: {e}")
    except UsernameForbiddenError as e:
        print(f"Caught Custom Error: {e}")
    except PasswordTooWeakError as e:
        print(f"Caught Custom Error: {e}")
    else:
        print("All registrations successful!")