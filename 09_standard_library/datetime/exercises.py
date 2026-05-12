"""
EXERCISES: The Time Traveler

EXERCISE 1: New Year Countdown
1. Calculate the current time.
2. Create a datetime object for the next January 1st.
3. Print how many days, hours, and minutes are left until the New Year.

EXERCISE 2: Age in Seconds
1. Ask for the user's birthdate (or use a dummy variable).
2. Calculate the difference between now and the birthdate.
3. Print the user's age in total seconds. (Hint: look at the .total_seconds() method).

EXERCISE 3: Weekday Finder
1. Write a function that takes a date string (e.g., "2025-05-10").
2. Return the name of the day of the week (e.g., "Saturday").
"""

# TODO: Implement the exercises below
from datetime import datetime, timedelta

def get_days_until_new_year():
    current_time = datetime.now()
    next_year = current_time.year + 1
    new_year = datetime(next_year, 1, 1)
    time_left = new_year - current_time
    return time_left

def get_age_in_seconds(birthdate: str):
    current_time = datetime.now()
    birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
    time_left = current_time - birth_date
    return time_left.total_seconds()

def get_weekday_name(date_str: str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    return date.strftime("%A")

if __name__ == "__main__":
    print(get_days_until_new_year())
    print(get_age_in_seconds("1990-05-10"))
    print(get_weekday_name("2026-05-12"))
