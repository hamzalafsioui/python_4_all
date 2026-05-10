"""
PROJECT: Unified Notification System

Goal: Create a system that can send notifications through different channels using a single interface.

Requirements:

1. Abstract Base Class 'BaseNotification':
   - Abstract method 'send(message)'.

2. Subclasses:
   - 'EmailNotification': Prints "Sending Email: [message]".
   - 'SMSNotification': Prints "Sending SMS: [message]".
   - 'SlackNotification': Prints "Posting to Slack: [message]".

3. Class 'NotificationManager':
   - Attribute 'subscribers': A list of notification objects.
   - Method 'add_subscriber(sub)': Adds a notification object to the list.
   - Method 'notify_all(message)': Loops through subscribers and calls .send(message) on each.

Real-World Logic:
- This pattern (The Observer Pattern) is used in real apps to send alerts, newsletters, or system updates without hardcoding each channel.
"""
from abc import ABC, abstractmethod

class BaseNotification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(BaseNotification):
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSNotification(BaseNotification):
    def send(self, message):
        print(f"Sending SMS: {message}")

class SlackNotification(BaseNotification):
    def send(self, message):
        print(f"Posting to Slack: {message}")

class NotificationManager:
    def __init__(self):
        self.subscribers = []
    
    def add_subscriber(self, sub):
        self.subscribers.append(sub)
    
    def notify_all(self, message):
        for sub in self.subscribers:
            sub.send(message)

# TODO: Implement the Notification System
if __name__ == "__main__":
    notification_manager = NotificationManager()
    notification_manager.add_subscriber(EmailNotification())
    notification_manager.add_subscriber(SMSNotification())
    notification_manager.add_subscriber(SlackNotification())
    notification_manager.notify_all("Hello World")
