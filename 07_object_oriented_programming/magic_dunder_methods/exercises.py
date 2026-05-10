"""
EXERCISES: The Magic Touch

EXERCISE 1: The Time Adder
1. Create a class 'Time' with 'hours' and 'minutes'.
2. Implement '__str__' to show time as "HH:MM".
3. Implement '__add__' to allow adding two Time objects. 
   - Hint: If minutes > 60, increment hours.

EXERCISE 2: The Comparison Game
1. Create a class 'Product' with 'name' and 'price'.
2. Implement '__gt__' (Greater Than) to compare products based on price.
3. Create a list of products and use Python's built-in 'max()' function on it. 
   - Note: 'max()' uses '__gt__' under the hood!

EXERCISE 3: The Custom List
1. Create a class 'Playlist' that holds a list of 'songs'.
2. Implement '__len__' and '__getitem__'.
3. Test it by calling 'len(my_playlist)' and 'my_playlist[0]'.
"""

class Time:
   def __init__(self,hours,minutes):
      self.hours = hours
      self.minutes = minutes
   
   def __str__(self):
      return f"{self.hours}:{self.minutes}"
   
   def __add__(self,other):
      new_hours = self.hours + other.hours
      new_minutes = self.minutes + other.minutes
      if new_minutes >= 60:
         new_hours += 1
         new_minutes -= 60
      return Time(new_hours,new_minutes)

class Product:
   def __init__(self,name,price):
      self.name = name
      self.price = price
   
   def __gt__(self,other):
      return self.price > other.price
   
   def __str__(self):
      return f"{self.name} costs {self.price}"
   
   def __repr__(self):
      return f"Product({self.name}, {self.price})"

class Playlist:
   def __init__(self,songs):
      self.songs = songs
   
   def __len__(self):
      return len(self.songs)
   
   def __getitem__(self,index):
      return self.songs[index]

# TODO: Implement the exercises below
if __name__ == "__main__":
   time1 = Time(1,30)
   time2 = Time(2,45)
   print(time1)
   print(time2)
   print(time1 + time2)

   product1 = Product("Laptop",1000)
   product2 = Product("Mouse",10)
   product3 = Product("Keyboard",50)
   print(product1 > product2)
   print(product1 > product3)

   playlist = Playlist(["Song 1","Song 2","Song 3"])
   print(len(playlist))
   print(playlist[0])
