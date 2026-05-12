"""
PROJECT: Event Countdown Manager

Goal: Create a system that tracks multiple events and shows their status.

Requirements:

1. Data Structure:
   - A list of events, where each event is a dictionary: 
     {"name": "Python Exam", "date": "2024-06-15"}

2. Logic:
   - Loop through each event.
   - Parse the date string into a datetime object.
   - Calculate the difference between the event date and 'now'.
   
3. Output:
   - If diff > 0: Print "[Upcoming] 'name' in X days".
   - If diff == 0 (same day): Print "[TODAY] 'name' is happening now!".
   - If diff < 0: Print "[Passed] 'name' was X days ago".

Bonus:
- Sort the events so the most recent upcoming event is at the top.
"""

# TODO: Implement the Event Manager
from datetime import datetime

events = [
    {"name": "Graduation", "date": "2025-07-20"},
    {"name": "Summer Break", "date": "2026-06-01"},
    {"name": "Project Deadline", "date": "2026-05-12"},
    {"name": "Birthday Party", "date": "2026-12-31"}
]

def days_until_event(events):
    now = datetime.now().date()
    for event in events:
        event_date = datetime.strptime(event["date"], "%Y-%m-%d").date()
        
        if event_date > now:
            print(f"[Upcoming] {event['name']} in {(event_date - now).days} days.")
        elif event_date == now:
            print(f"[TODAY] {event['name']} is happening now!")
        else:
            print(f"[Passed] {event['name']} was {(now - event_date).days} days ago.")


if __name__ == "__main__":
    days_until_event(events)
