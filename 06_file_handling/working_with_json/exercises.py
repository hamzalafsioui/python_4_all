"""
EXERCISES: The Configuration Updater

Task:
1. Create a file named 'config.json' with the following content:
   {
       "theme": "dark",
       "font_size": 14,
       "show_notifications": true
   }
2. Read the file into a Python dictionary.
3. Update the 'font_size' to 18.
4. Add a new key 'language' with the value 'English'.
5. Save the updated dictionary back to 'config.json' with an indentation of 4 spaces.
"""

# TODO: Implement the config updater
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

def update_config():
    # TODO: Implement this
    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)
    config["font_size"] = 18
    config["language"] = "English"
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    update_config()
