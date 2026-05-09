"""
PROJECT: Secure Employee Record System

Goal: Manage sensitive employee data without exposing it directly.

Requirements:

1. Class 'Employee':
   - Attributes: 'name' (public), '_department' (protected), '__salary' (private).
   - Method 'set_salary(new_salary)': 
     - Only allows changes if the caller provides a secret 'admin_code'.
   - Method 'get_salary()':
     - Formats the salary as "$XX,XXX".
   - Method 'promote()':
     - Increases salary by 10% internally.

2. Logic:
   - Create an employee.
   - Try to change their salary directly (it should fail or be discouraged).
   - Use the authorized methods to update and view the salary.

Professional Touch:
- Use docstrings to explain why the salary is private.
- Implement @property for the salary if you prefer the modern Python way.
"""
class Employee:
    """
    A class representing an employee with private salary.
    """
    def __init__(self, name, department, salary):
        self.name = name
        self._department = department
        self.__salary = salary
    
    @property
    def salary(self):
        return f"${self.__salary:,.0f}"

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary
    
    def promote(self):
        self.__salary *= 1.1


# TODO: Implement the Secure Employee system

if __name__ == "__main__":
    employee = Employee("Hamza", "Engineering", 1000)
    print(employee.salary)
    employee.promote()
    print(employee.salary)
    employee.salary = 2000
    print(employee.salary)
    employee.salary = 3000
    print(employee.salary)
    employee.salary = 5000
    print(employee.salary)
