# Examples: Inheriting Behavior

class Employee:
    """Base class for all company employees."""
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def work(self):
        return f"{self.name} is performing general tasks."

class Developer(Employee):
    """Subclass representing a software engineer."""
    def __init__(self, name, salary, programming_language):
        # Use super() to initialize name and salary from Employee
        super().__init__(name, salary)
        self.language = programming_language
        
    def work(self):
        # Overriding the parent method
        return f"{self.name} is writing code in {self.language}."

class Manager(Employee):
    """Subclass representing a manager."""
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
        
    def work(self):
        # Overriding and extending
        parent_msg = super().work() # You can still use the parent's logic!
        return f"{parent_msg} Specifically, managing a team of {self.team_size}."

# --- Usage ---
dev = Developer("Hamza", 80000, "Python")
mgr = Manager("Ali", 100000, 10)

employees = [dev, mgr]

print("--- Daily Work Log ---")
for emp in employees:
    print(emp.work())

# Relationship Checks
print(f"\nIs 'dev' an Employee? {isinstance(dev, Employee)}")
print(f"Is 'Developer' a subclass of Employee? {issubclass(Developer, Employee)}")
