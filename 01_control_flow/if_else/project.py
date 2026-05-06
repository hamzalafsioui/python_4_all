"""
Mini-Project: Movie Ticket Booking System

In this project, you will simulate a movie theater ticket booking system.
The price of the ticket depends on the age of the customer and whether they have a coupon.

"""

# ============= (1) Input Data ===========
customer_age = 22
has_coupon = True
movie_rating = "R"  # G, PG, PG-13, R

# ============== (2) Base Ticket Price =============
# Standard: $12
# Senior (65+): $8
# Child (Under 12): $7

# Your logic here:
if customer_age >= 65:
    price = 8
elif customer_age < 12:
    price = 7
else:
    price = 12

# ============== (3) Apply Coupon Discount =============
# If has_coupon is True, subtract $2 from the price.
if has_coupon:
    price -= 2

# ============== (4) Check Age Requirements for Movie Rating =============
# G: Anyone
# PG/PG-13: Anyone (with guidance, but we'll allow it for this demo)
# R: Must be 18 or older
can_watch = True

if movie_rating == "R" and customer_age < 18:
    can_watch = False

# ============== (5) Print the Invoice =============
print("=" * 30)
print("     CINEMA TICKETING")
print("=" * 30)
print(f"Age:           {customer_age}")
print(f"Movie Rating:  {movie_rating}")
print(f"Coupon:        {'Applied' if has_coupon else 'None'}")
print("-" * 30)

if can_watch:
    print(f"TOTAL PRICE:   ${price}")
    print("Enjoy your movie!")
else:
    print("ACCESS DENIED!")
    print("You are not old enough to watch this movie.")

print("=" * 30)
