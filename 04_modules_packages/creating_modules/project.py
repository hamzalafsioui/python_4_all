"""
PROJECT: Mini Banking System

Goal: Split a simple bank logic into two files.

Requirements:
1. 'bank_logic.py': 
   - A variable 'balance' initialized to 1000.
   - A function 'deposit(amount)' that adds to balance.
   - A function 'withdraw(amount)' that subtracts from balance.
2. 'project.py' (This file):
   - Import the functions from 'bank_logic'.
   - Create a simple loop where the user can choose to deposit, withdraw, or check balance.
"""

# TODO: Implement the project
print("Banking System Project initialized.")

import bank_logic

choix = input(" enter your choice\n1_deposit\n2_withdraw\n3_check balance\n")

while choix != "q":
    if choix == "1":
        amount = float(input("Enter amount to deposit: "))
        bank_logic.deposit(amount)
        print(f"New balance: {bank_logic.balance}")
    elif choix == "2":
        amount = float(input("Enter amount to withdraw: "))
        bank_logic.withdraw(amount)
        print(f"New balance: {bank_logic.balance}")
    elif choix == "3":
        print(f"Current balance: {bank_logic.balance}")
    else:
        print("Invalid choice.")
    choix = input("Enter your choice (q to quit): ")
