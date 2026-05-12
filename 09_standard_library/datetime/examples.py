# Examples: Working with Dates and Times

from datetime import datetime, date, timedelta

# 1_ Current Time and Basic Formatting
def now_demo():
    print("--- Current Time ---")
    now = datetime.now()
    today = date.today()
    
    print(f"Full Datetime: {now}")
    print(f"Just Date:     {today}")
    
    # Custom Formatting
    print(f"Readable: {now.strftime('%A, %B %d, %Y')}")
    print(f"Time only: {now.strftime('%I:%M %p')}")

# 2_ Time Arithmetic (Timedelta)
def math_demo():
    print("\n--- Time Arithmetic ---")
    now = datetime.now()
    
    # Add 100 days
    future = now + timedelta(days=100)
    print(f"100 days from now: {future.date()}")
    
    # Subtract 5 hours and 30 minutes
    past = now - timedelta(hours=5, minutes=30)
    print(f"5.5 hours ago: {past.strftime('%H:%M')}")
    
    # Difference between two dates
    birthday = datetime(now.year, 12, 25)
    diff = birthday - now
    print(f"Days until Dec 25th: {diff.days}")

# 3_ Parsing Strings
def parsing_demo():
    print("\n--- Parsing Strings ---")
    user_input = "2024-01-01 12:00:00"
    
    # String -> Object
    dt_object = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
    print(f"Parsed Object: {type(dt_object)}")
    print(f"Year: {dt_object.year}")

# --- Usage ---

if __name__ == "__main__":
    now_demo()
    math_demo()
    parsing_demo()
