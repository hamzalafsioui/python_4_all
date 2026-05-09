# Examples: Access Control & Name Mangling

class BankAccount:
    def __init__(self, owner, amount):
        self.owner = owner          # Public
        self._account_type = "Gold" # Protected
        self.__balance = amount     # Private (Name Mangled)
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
            
    def get_balance(self):
        """Secure way to check balance."""
        return self.__balance

# --- Usage ---
acc = BankAccount("Hamza", 1000)

# 1_ Accessing Public
print(f"Owner: {acc.owner}")

# 2_ Accessing Protected (Technically works, but don't do it!)
print(f"Type: {acc._account_type}")

# 3_ Accessing Private (Fails!)
try:
    print(acc.__balance)
except AttributeError:
    print("Error: Cannot access __balance directly!")

# 4_ The "Secret" Mangled Name (Don't use this in real code!)
# Python renames __balance to _BankAccount__balance
print(f"Secret Access: {acc._BankAccount__balance}")

# 5_ The Proper Way
print(f"Proper Access: {acc.get_balance()}")
