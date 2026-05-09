"""
EXERCISES: Class Masters

EXERCISE 1: The Circle with Class Data
1. Create a class 'Circle'.
2. Add a class attribute 'PI = 3.14159'.
3. In '__init__', set the instance attribute 'radius'.
4. Add an instance method 'area()' that uses the class attribute 'PI'.
5. Add a class method 'from_diameter(cls, diameter)' that returns a new Circle instance.

EXERCISE 2: Temperature with Static Methods
1. Create a class 'TemperatureConverter'.
2. Add a static method 'celsius_to_fahrenheit(c)'.
3. Add a static method 'fahrenheit_to_celsius(f)'.
4. Test them without creating an instance of the class.

EXERCISE 3: The Secure User (Property)
1. Create a class 'User'.
2. Use a "private" attribute '_username'.
3. Use '@property' to allow reading 'username'.
4. Use '@username.setter' to ensure the username is at least 3 characters long.
"""

class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius * self.radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)


class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9


class User:

    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if len(username) < 3:
            raise ValueError(
                "Username must be at least 3 characters long"
            )

        self._username = username


if __name__ == "__main__":

    c1 = Circle(5)
    print(c1.area())

    c2 = Circle.from_diameter(10)
    print(c2.area())

    print(TemperatureConverter.celsius_to_fahrenheit(0))
    print(TemperatureConverter.fahrenheit_to_celsius(32))

    u = User("hamza")

    print(u.username)

    u.username = "hah"

    print(u.username)