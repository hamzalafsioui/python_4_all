"""
EXERCISES: The Hierarchy Architect

EXERCISE 1: The Animal Kingdom
1. Create a base class 'Animal' with 'name' and a method 'speak()'.
2. Create a subclass 'Dog' that overrides 'speak()' to return "Woof!".
3. Create a subclass 'Cat' that overrides 'speak()' to return "Meow!".

EXERCISE 2: Shapes & Areas
1. Create a base class 'Shape' with an 'color' attribute.
2. Create a subclass 'Rectangle' (width, height) and 'Circle' (radius).
3. Ensure both subclasses use 'super()' to set the color.
4. Give both subclasses an 'area()' method.

EXERCISE 3: Checking Types
1. Create a list containing a Dog, a Cat, and a Rectangle.
2. Iterate through the list and only call 'speak()' if the object is an instance of Animal.
"""

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


class Shape:
    def __init__(self, color):
        self.color = color
    
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# TODO: Implement the exercises below
if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    rectangle = Rectangle("Red", 10, 20)
    circle = Circle("Blue", 5)

    print(dog.speak())
    print(cat.speak())

    print(rectangle.area())
    print(circle.area())

    animals = [dog, cat, rectangle, circle]
    for animal in animals:
        if isinstance(animal, Animal):
            print(animal.speak())
