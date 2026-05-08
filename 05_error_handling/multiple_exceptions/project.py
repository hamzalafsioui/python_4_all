"""
PROJECT: Secure Configuration Loader

Goal: Write a function that safely reads values from a nested dictionary (simulating a config file).

Requirements:
1. Function `get_config_value(config, path_string, default=None)`:
   - `path_string` is a string like "database.port" or "server.host".
   - Split the path and navigate through the nested `config` dictionary.
   - Handle cases where keys are missing or the structure isn't what you expect (e.g., trying to index into a string).
   - Return the `default` value if any error occurs during navigation.

Example:
cfg = {"db": {"host": "localhost", "port": 5432}}
get_config_value(cfg, "db.host") -> "localhost"
get_config_value(cfg, "db.user", "admin") -> "admin"
get_config_value(cfg, "db.host.ip") -> None (since host is a string, not a dict)
"""

# TODO: Implement the project

def get_config_value(config, path_string, default=None):
    try:
        keys = path_string.split('.')
        current_value = config
        for key in keys:
            current_value = current_value[key]
        return current_value
    except (KeyError, TypeError):
        print(f"Error: Path '{path_string}' is invalid or missing!")
        return default

# Test Cases
cfg = {"db": {"host": "localhost", "port": 5432}}

print(get_config_value(cfg, "db.host"))
print(get_config_value(cfg, "db.user", "admin"))
print(get_config_value(cfg, "db.host.ip"))

