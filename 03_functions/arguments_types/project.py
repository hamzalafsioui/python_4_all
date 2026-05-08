"""
Mini-Project: Dynamic Event Scheduler

This project demonstrates handling optional and variable configuration 
using different argument types.
"""

def schedule_event(title, date, venue="TBD", *guests, **extra_details):
    """
    Schedules an event with various configuration options.
    """
    print("=" * 40)
    print(f" EVENT: {title.upper()}")
    print(f" DATE:  {date}")
    print(f" VENUE: {venue}")
    print("-" * 40)
    
    # Handle *guests
    if guests:
        print(" GUESTS:")
        for guest in guests:
            print(f" - {guest}")
    
    # Handle **extra_details
    if extra_details:
        print("\n ADDITIONAL INFO:")
        for key, value in extra_details.items():
            print(f" - {key.replace('_', ' ').capitalize()}: {value}")
    
    print("=" * 40)

# --- Simulation ---

# 1. Minimal event
schedule_event("Python Meetup", "2024-06-15")

# 2. Event with specific venue and guest list
schedule_event(
    "Tech Workshop", 
    "2024-07-20", 
    "Casablanca Hub", 
    "Ali", "Hamza", "Zakaria"
)

# 3. Full event with extra keyword details
schedule_event(
    "AI Summit",
    "2024-12-01",
    "Grand Hotel",
    "Elon", "Sam", "Jensen", # *guests
    ticket_price="$200",      # **extra_details
    lunch_included=True,
    parking="Free"
)
