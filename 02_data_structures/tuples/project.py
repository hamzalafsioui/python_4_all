"""
Mini-Project: Geographic Coordinate Tracker

In this project, we use tuples to store and process constant data like 
geographic coordinates (Latitude, Longitude).
"""

# 1_ Define a list of locations as tuples
# Format: (Location Name, (Lat, Long))
locations = [
    ("Eiffel Tower", (48.8584, 2.2945)),
    ("Statue of Liberty", (40.6892, -74.0445)),
    ("Pyramids of Giza", (29.9792, 31.1342))
]

print("=" * 40)
print("     WORLD COORDINATE TRACKER")
print("=" * 40)

# 2_ Process the data using unpacking
for name, coords in locations:
    lat, lon = coords # Nested unpacking
    
    # Determine Hemisphere
    ns = "North" if lat >= 0 else "South"
    ew = "East" if lon >= 0 else "West"
    
    print(f">>> {name}")
    print(f"Coords: {lat}° {ns}, {lon}° {ew}")
    print(f"Region: {ns}ern & {ew}ern Hemisphere")
    print("-" * 40)

# 3_ Search for a specific location
search_name = "Pyramids of Giza"
for name, coords in locations:
    if name == search_name:
        print(f"\nFOUND {search_name.upper()}!")
        print(f"Target Lat: {coords[0]}")
        print(f"Target Lon: {coords[1]}")

print("=" * 40)
