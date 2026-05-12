"""
EXERCISES: The CLI Architect

EXERCISE 1: The Area Calculator
1. Build a script that takes 'width' and 'height' as positional arguments.
2. Ensure both are treated as floats.
3. Calculate and print the area.
4. Test: python exercises.py 10.5 5.0

EXERCISE 2: The Multi-Printer
1. Build a script that takes a 'text' string.
2. Add an optional '--count' argument (type=int, default=1).
3. Print the 'text' exactly 'count' times.

EXERCISE 3: The Restricted Operation
1. Build a script that takes two numbers and an '--op' argument.
2. Use 'choices=["add", "sub", "mul"]' for the '--op' argument.
3. Perform the math and print the result.
"""

# TODO: Implement the exercises below
import argparse

# Exercise 1
def demo_ex1():
    parser = argparse.ArgumentParser(description="Calculate the area of a rectangle.")
    parser.add_argument("width", type=float, help="Width of the rectangle")
    parser.add_argument("height", type=float, help="Height of the rectangle")
    args = parser.parse_args()
    print(args.width * args.height)

# Exercise 2
def demo_ex2():
    parser = argparse.ArgumentParser(description="Print text multiple times.")
    parser.add_argument("text", help="Text to print")
    parser.add_argument("--count", type=int, default=1, help="Number of times to print")
    args = parser.parse_args()
    for _ in range(args.count):
        print(args.text)

# Exercise 3
def demo_ex3():
    parser = argparse.ArgumentParser(description="Perform a restricted math operation.")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    parser.add_argument("--op", choices=["add", "sub", "mul"], required=True, help="Operation to perform")
    args = parser.parse_args()
    if args.op == "add":
        print(args.num1 + args.num2)
    elif args.op == "sub":
        print(args.num1 - args.num2)
    elif args.op == "mul":
        print(args.num1 * args.num2)

if __name__ == "__main__":
    # demo_ex1()
    # demo_ex2()
    demo_ex3()
