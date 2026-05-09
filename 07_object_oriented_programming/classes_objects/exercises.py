"""
EXERCISES: The Smart Home & Geometry

EXERCISE 1: The Smart Light
Create a class 'SmartLight' with:
1. Attributes: 'room', 'brightness' (0 to 100), and 'is_on' (boolean).
2. Methods:
   - turn_on() / turn_off()
   - set_brightness(level): Ensure level stays between 0 and 100.
   - status(): Prints if the light is on and at what brightness.

EXERCISE 2: The Rectangle
Create a class 'Rectangle' with:
1. Attributes: 'width', 'height'.
2. Methods:
   - area(): Returns width * height.
   - perimeter(): Returns 2 * (width + height).
   - is_square(): Returns True if width == height.
"""

# TODO: Implement the classes and test them below
class SmartLight:
    def __init__(self, room, brightness=50, is_on=False):
        self.room = room
        self.brightness = brightness
        self.is_on = is_on

    def turn_on(self):
        self.is_on = True
        print(f"{self.room} light turned on.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.room} light turned off.")

    def set_brightness(self, level):
        if level < 0 or level > 100:
            print("Error: Brightness must be between 0 and 100.")
        else:
            self.brightness = level
            print(f"{self.room} brightness set to {self.brightness}.")

    def status(self):
        if self.is_on:
            print(f"{self.room} is ON at {self.brightness} brightness.")
        else:
            print(f"{self.room} is OFF.")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

if __name__ == "__main__":
    # Test your code here

    smartlight = SmartLight("Living Room")
    smartlight.turn_on()
    smartlight.set_brightness(50)
    smartlight.status()

    rectangle = Rectangle(10, 10)
    print(f"Area: {rectangle.area()}")
    print(f"Perimeter: {rectangle.perimeter()}")
    print(f"Is Square: {rectangle.is_square()}")
