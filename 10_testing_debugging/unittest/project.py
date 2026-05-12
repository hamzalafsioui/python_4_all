"""
PROJECT: Bank Account Test Suite

Goal: Create a BankAccount class and a full suite of tests to ensure financial safety.

Requirements:

1. The Class 'BankAccount':
   - '__init__(balance)': Set initial balance.
   - 'deposit(amount)': Add money.
   - 'withdraw(amount)': Subtract money. Raise 'ValueError' if balance is insufficient.
   - 'get_balance()': Return current balance.

2. The Test Suite 'TestBankAccount':
   - Use 'setUp()' to create a new BankAccount(100) before every test.
   - Test 'deposit': Ensure balance increases correctly.
   - Test 'withdraw_success': Ensure money is removed correctly.
   - Test 'withdraw_insufficient': Ensure ValueError is raised when withdrawing too much.
   - Test 'get_balance': Ensure it matches expectation.

Real-World Logic:
- Financial software REQUIRES 100% test coverage. Every possible transaction must be tested before it goes live.
"""

import unittest

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
    
    def get_balance(self):
        return self.balance

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)
    
    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)
    
    def test_withdraw_success(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), 50)
    
    def test_withdraw_insufficient(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150)
    
    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

if __name__ == "__main__":
    unittest.main()
