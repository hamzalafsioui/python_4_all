"""
PROJECT: Fleet Management System

Goal: Track a fleet of vehicles and calculate total maintenance costs.

Requirements:

1. Class 'Vehicle':
   - Class Attribute: 'total_vehicles' (int, starts at 0).
   - Class Attribute: 'base_maintenance_cost' (e.g., 50.0).
   - In '__init__', increment 'total_vehicles'.
   - Instance Attributes: 'make', 'model', 'mileage'.
   - Instance Method: 'calculate_maintenance()'. 
     - Logic: base_maintenance_cost + (0.05 * mileage).
   
2. Class 'Fleet':
   - Attribute 'vehicles': A list of Vehicle objects.
   - Method 'add_vehicle(vehicle)': Adds to list.
   - Method 'total_fleet_maintenance()': Sums maintenance costs of all vehicles.
   
3. Best Practice:
   - Use a @classmethod to update the 'base_maintenance_cost' for all vehicles if inflation hits.
   - Use @property to ensure 'mileage' cannot be set to a negative number.
"""

class Vehicle:
    total_vehicles = 0
    base_maintenance_cost = 50.0

    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage  # uses property setter
        Vehicle.total_vehicles += 1

    # PROPERTY: mileage cannot be negative
    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value < 0:
            raise ValueError("Mileage cannot be negative.")
        self._mileage = value

    def calculate_maintenance(self):
        return Vehicle.base_maintenance_cost + (0.05 * self.mileage)

    # CLASS METHOD: update shared maintenance cost
    @classmethod
    def update_base_maintenance_cost(cls, new_cost):
        cls.base_maintenance_cost = new_cost


class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def total_fleet_maintenance(self):
        return sum(v.calculate_maintenance() for v in self.vehicles)


# Example usage
if __name__ == "__main__":
    v1 = Vehicle("Toyota", "Camry", 10000)
    v2 = Vehicle("Honda", "Accord", 20000)

    f = Fleet()
    f.add_vehicle(v1)
    f.add_vehicle(v2)

    print(f.total_fleet_maintenance())

    Vehicle.update_base_maintenance_cost(100)

    print(f.total_fleet_maintenance())