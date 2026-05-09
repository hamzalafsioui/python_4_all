# Examples: Real-World Classes

class CoffeeMachine:
    """A virtual coffee machine for the office."""
    
    def __init__(self, model_name, water_capacity):
        self.model = model_name
        self.water_capacity = water_capacity  # in ml
        self.water_level = 0                  # current water
        self.is_on = False
        
    def power_button(self):
        self.is_on = not self.is_on
        status = "ON" if self.is_on else "OFF"
        print(f"[{self.model}] Power is now {status}.")
        
    def fill_water(self, amount):
        if self.water_level + amount > self.water_capacity:
            print(f"Error: Maximum capacity is {self.water_capacity}ml!")
            self.water_level = self.water_capacity
        else:
            self.water_level += amount
            print(f"Water filled. Current level: {self.water_level}ml.")
            
    def brew_coffee(self):
        if not self.is_on:
            print("Error: Turn on the machine first!")
            return
            
        if self.water_level < 250:
            print("Error: Not enough water for a cup (need 250ml).")
        else:
            self.water_level -= 250
            print("Brewing a fresh cup of coffee... Done!")

# --- Usage ---
print("--- Creating Office Machine ---")
office_mac = CoffeeMachine("DeLonghi Pro", 1000)

office_mac.power_button()
office_mac.fill_water(500)
office_mac.brew_coffee()
office_mac.brew_coffee()
office_mac.brew_coffee() # This should fail (low water)

print(f"\nFinal State: {office_mac.water_level}ml left.")
