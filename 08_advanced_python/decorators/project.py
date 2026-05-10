"""
PROJECT: Advanced Access Control System

Goal: Secure sensitive functions using an authentication decorator.

Requirements:

1. Global state: 'current_user' (None by default).
2. Decorator '@require_auth':
   - Checks if 'current_user' is not None.
   - If user exists, allows the function to run.
   - If 'current_user' is None, raises an PermissionError (or prints an error).
3. Decorator '@require_admin':
   - Checks if 'current_user' is "admin".
   - Only allows execution if the condition is met.

Functions to Protect:
- 'view_dashboard()': Requires any auth.
- 'delete_user()': Requires admin auth.

Real-World Logic:
- This simulates how frameworks like Flask or Django protect routes/views.
"""

# TODO: Implement the Access Control System
from functools import wraps

current_user = None # Global state for simulation


def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user:
            print(f"User {current_user} is logged in!")
            return func(*args, **kwargs)
        else:
            print("No user is logged in!")
            raise PermissionError("User not logged in")
    return wrapper    
    

def require_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user == "admin":
            print("Admin access granted!")
            return func(*args, **kwargs)
        else:
            print("Admin access denied!")
            raise PermissionError("User is not admin")
    return wrapper

@require_auth
def view_dashboard():
    print("Dashboard view accessed!")
    return "Dashboard data"  
    
@require_admin
@require_auth
def delete_user():
    print("User deleted!")
    return "User deleted"

if __name__ == "__main__":
    # Test 1: No user
    try:
        print("Test 1: No user")
        current_user = None
        view_dashboard()
        delete_user()
    except PermissionError as e:
        print(e)
    
    # Test 2: Regular user
    try:
        print("\nTest 2: Regular user")
        current_user = "user"
        view_dashboard()
        delete_user()
    except PermissionError as e:
        print(e)
    
    # Test 3: Admin user
    try:
        print("\nTest 3: Admin user")
        current_user = "admin"
        view_dashboard()
        delete_user()
    except PermissionError as e:
        print(e)
