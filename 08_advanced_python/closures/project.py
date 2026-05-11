"""
PROJECT: Secure Configuration Manager

Goal: Use closures to create a configuration system that protects data from direct modification.

Requirements:

1. Function 'create_config()':
   - Contains a private dictionary 'settings' (e.g., {"api_key": "12345", "timeout": 30}).
   - Returns TWO functions:
     1. 'get(key)': Returns the value of a key.
     2. 'set(key, value)': Updates a key.
   
2. Logic:
   - The 'settings' dictionary should NOT be accessible from outside the 'create_config' scope.
   - The only way to interact with it is through the returned 'get' and 'set' functions.

Real-World Logic:
- This pattern is common in JavaScript and some Python libraries to encapsulate private state without using Classes. It's called the "Module Pattern."
"""

# TODO: Implement the Secure Config Manager

def create_config():
    settings = {
        "api_key": "12345",
        "timeout": 30
    }
    
    def get(key):
        return settings.get(key)
    
    def set(key, value):
        settings[key] = value
        return settings
    
    return get, set


if __name__ == "__main__":
    get, set = create_config()
    print(get("api_key"))
    set("api_key", "67890")
    print(get("api_key"))
