"""
PROJECT: Smart Wallet System

Goal: Create a Wallet class that supports mathematical operations and comparisons.

Requirements:

1. Class 'Wallet':
   - Attribute 'balance' (float).
   - Attribute 'currency' (string, e.g., "USD").
   - '__str__': Show balance and currency (e.g., "Balance: 50.00 USD").
   - '__add__': Adding two wallets of the SAME currency should return a new Wallet.
   - '__eq__': Wallets are equal if they have the same balance and currency.
   - '__gt__': Compare wallets based on balance.

Real-World Logic:
- Raise a ValueError if the user tries to add two wallets with DIFFERENT currencies.
- This prevents "adding apples to oranges" (or Dollars to Euros) without a conversion step.

Bonus:
- Implement '__sub__' for spending money.
- Add a check in '__sub__' to prevent a negative balance.
"""
class Wallet:
    def __init__(self,balance,currency):
        self.balance = balance
        self.currency = currency
    
    def __str__(self):
        return f"{self.balance} {self.currency}"
    
    def __add__(self,other):
        if self.currency != other.currency:
            raise ValueError("Wallets must have the same currency")
        return Wallet(self.balance + other.balance,self.currency)
    
    def __eq__(self,other):
        return self.balance == other.balance and self.currency == other.currency
    
    def __gt__(self,other):
        return self.balance > other.balance
    
    def __sub__(self,other):
        if self.currency != other.currency:
            raise ValueError("Wallets must have the same currency")
        if self.balance < other.balance:
            raise ValueError("Negative balance is not allowed")
        return Wallet(self.balance - other.balance,self.currency)

# TODO: Implement the Smart Wallet System
if __name__ == "__main__":
    wallet1 = Wallet(100,"USD")
    wallet2 = Wallet(200,"USD")
    print(wallet1)
    print(wallet2)
    print(wallet1 + wallet2)
    print(wallet1 == wallet2)
    print(wallet1 > wallet2)
    print(wallet2 - wallet1)

    try:
        print(wallet1 - wallet2)
    except ValueError as e:
        print(e)
