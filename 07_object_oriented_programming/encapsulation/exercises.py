"""
EXERCISES: The Secure Shield

EXERCISE 1: The Secure User
1. Create a class 'User' with:
   - Public: 'username'
   - Private: '__password'
2. Create a method 'check_password(input_pwd)' that returns True if it matches.
3. Try to access '__password' directly from outside and catch the error.

EXERCISE 2: Controlled Temperature
1. Create a class 'Thermostat'.
2. Use a protected attribute '_temp'.
3. Use '@property' for 'temp'.
4. Use '@temp.setter' to ensure the temperature stays between 0 and 100.
5. If the user tries to set it higher or lower, print a warning and don't change it.
"""
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
    
    def check_password(self, password):
        return self.__password == password

class Thermostat:
    def __init__(self, temp):
        self._temp = temp
    
    @property
    def temp(self):
        return self._temp
    
    @temp.setter
    def temp(self, temp):
        if temp < 0 or temp > 100:
            print("Temperature must be between 0 and 100.")
        else:
            self._temp = temp

# TODO: Implement the exercises below
if __name__ == "__main__":
   
   user = User("hamza", "1234")
   print(user.check_password("1234"))
   print(user._User__password)

   
   thermostat = Thermostat(25)
   print(thermostat.temp)
   thermostat.temp = 110
   thermostat.temp = 45
   print(thermostat.temp)
