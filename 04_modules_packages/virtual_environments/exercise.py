"""
EXERCISE: The Package Manager

1. Create a virtual environment named 'practice_env'.
2. Activate it.
3. Install the 'colorama' package using pip.
4. Create a small script that uses colorama to print text in RED.
5. Deactivate the environment.
"""

# TODO: Document your steps here or write a script that tests if colorama is installed
try:
    from colorama import Fore, Style
    print(Fore.RED + "This exercise is working in a venv!" + Style.RESET_ALL)
except ImportError:
    print("Colorama not found. Did you activate your venv and install it?")
