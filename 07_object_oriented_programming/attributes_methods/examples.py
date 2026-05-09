# Examples: Class Data and Method Types

class Employee:
    # Class Attributes
    company_name = "TechCorp"
    number_of_employees = 0
    raise_amount = 1.05  # 5% raise
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"
        
        # Increment the class attribute every time a new employee is created
        Employee.number_of_employees += 1
        
    def apply_raise(self):
        """Instance Method: Uses class attribute but can be overridden by instance."""
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def set_raise_amt(cls, amount):
        """Class Method: Changes the raise for EVERYONE at once."""
        cls.raise_amount = amount
        
    @staticmethod
    def is_workday(day):
        """Static Method: Logic related to employees but doesn't need 'self' or 'cls'."""
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# --- Usage ---
emp_1 = Employee("Hamza", "Dev", 50000)
emp_2 = Employee("Ali", "Designer", 60000)

print(f"Total Employees: {Employee.number_of_employees}")

# Using Class Method
Employee.set_raise_amt(1.10) # 10% raise for everyone
print(f"New Global Raise Amount: {Employee.raise_amount}")

# Using Static Method
import datetime
my_date = datetime.date(2026, 5, 10) # A Sunday
print(f"Is {my_date} a workday? {Employee.is_workday(my_date)}")

# Using Instance Attribute Override
emp_1.raise_amount = 1.20 # Specialized raise just for Hamza
emp_1.apply_raise()
emp_2.apply_raise()

print(f"{emp_1.first}'s new pay: {emp_1.pay}") # 20% applied
print(f"{emp_2.first}'s new pay: {emp_2.pay}") # 10% applied
