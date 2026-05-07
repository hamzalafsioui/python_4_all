"""
Mini-Project: Simple Email Filter Simulator

In this project, we will process a list of "emails". 
- We will 'continue' (skip) emails marked as SPAM.
- We will 'break' (stop processing) if we encounter a MALICIOUS email.
- We will 'pass' (placeholder) for ARCHIVED emails.
"""

# 1_ Email Inbox (List of Tuples: (Sender, Content, Tag))
inbox = [
    ("Hamza", "Hey, how are you?", "NORMAL"),
    ("Ali", "WIN A FREE IPHONE!", "SPAM"),
    ("Aya", "Meeting at 5?", "NORMAL"),
    ("Hicham", "Logs from 2010", "ARCHIVED"),
    ("Zakaria", "CLICK HERE FOR VIRUS", "MALICIOUS"),
    ("Naim", "Don't forget the cake!", "NORMAL")
]

print("=" * 40)
print("       EMAIL PROCESSOR")
print("=" * 40)

# 2_ Processing Logic
for sender, content, tag in inbox:
    if tag == "MALICIOUS":
        print(f"\n[!!!] ALERT: Malicious email from {sender} detected!")
        print("Shutting down processor for safety...")
        break
    
    if tag == "SPAM":
        # Skip the rest of this loop and go to the next email
        continue
    
    if tag == "ARCHIVED":
        # We'll handle archived emails in Version 2_0
        pass
    else:
        # Process normal email
        print(f"\nFrom:    {sender}")
        print(f"Content: {content}")

print("-" * 40)
print("Processor finished.")
print("=" * 40)
