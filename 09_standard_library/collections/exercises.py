"""
EXERCISES: The Collection Architect

EXERCISE 1: The Word Counter
1. Take a long sentence from the user (or a variable).
2. Use 'Counter' to find the 3 most frequent words.
3. Print them clearly.

EXERCISE 2: Student Database
1. Use 'namedtuple' to create a 'Student' type with 'name', 'id', and 'major'.
2. Create a list of 3 students.
3. Iterate through the list and print "[ID] Name is majoring in Major".

EXERCISE 3: Alphabetical Grouping
1. Take a list of names: ["Alice", "Bob", "Charlie", "Anna", "Ben"].
2. Use 'defaultdict' to group them by their first letter.
   Result should be: {'A': ['Alice', 'Anna'], 'B': ['Bob', 'Ben'], ...}
"""

# TODO: Implement the exercises below
from collections import Counter, namedtuple, defaultdict
from collections import deque


if __name__ == "__main__":
    # EXERCISE 1: The Word Counter
    counter = Counter("I am a student and I am a good boy")
    print(counter.most_common(3))

    # EXERCISE 2: Student Database
    student = namedtuple("Student", ["name", "id", "major"])
    students = [
        student("Hamza", "123", "Computer Science"),
        student("Osama", "456", "Physics"),
        student("Ali", "789", "Chemistry")
    ]

    for s in students:
        print(f"{s.id} {s.name} is majoring in {s.major}")

    # EXERCISE 3: Alphabetical Grouping
    grouped = defaultdict(list)
    for name in ["Hamza", "Osama", "Ali", "Sara", "Fatima"]:
        grouped[name[0]].append(name)
    print(grouped)

    # EXERCISE 4: The Cache (Deque)
    dq = deque(maxlen=3)
    dq.append("Page 1")
    dq.append("Page 2")
    dq.append("Page 3")
    dq.append("Page 4") # Removes "Page 1"
    print(dq)

