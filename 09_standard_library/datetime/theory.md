# The Datetime Module: Managing Time

Handling dates and times is notoriously difficult in programming (time zones, leap years, formatting). Python's `datetime` module simplifies this by providing robust classes for date and time manipulation.

---

## 1. Core Classes
- **`date`**: Handles only Year, Month, and Day (e.g., 2023-12-25).
- **`time`**: Handles only Hour, Minute, Second, and Microsecond.
- **`datetime`**: A combination of both date and time.
- **`timedelta`**: Represents a **duration** (the difference between two dates or times).

---

## 2. Formatting and Parsing (The Big Two)
To move between strings and datetime objects, we use two methods:

### `strftime` (String **FROM** Time)
Used to turn a datetime object into a readable string.
```python
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M")) # Output: 2023-10-25 14:30
```

### `strptime` (String **PARSE** Time)
Used to turn a string into a datetime object.
```python
date_str = "25/12/2023"
dt_obj = datetime.strptime(date_str, "%d/%m/%Y")
```

---

## 3. Time Arithmetic (`timedelta`)
You can add or subtract time using `timedelta`.
```python
from datetime import datetime, timedelta

tomorrow = datetime.now() + timedelta(days=1)
last_week = datetime.now() - timedelta(weeks=1)
```

---

## 4. Unix Timestamps
A timestamp is the number of seconds since **January 1, 1970** (the "Epoch"). It is the universal way computers store time.
- `dt.timestamp()`: Object -> Seconds.
- `datetime.fromtimestamp(1698241200)`: Seconds -> Object.

---

## 5. Best Practices
1. **Always use UTC**: When saving to a database, use `datetime.now(timezone.utc)`. Convert to local time only when showing it to the user.
2. **Standard Formats**: Use ISO 8601 (`YYYY-MM-DD`) for storing dates whenever possible.
3. **Avoid Manual Math**: Never try to calculate "seconds in a month" manually. Use `timedelta` or third-party libraries like `dateutil`.

## Resources

- **Official Python datetime Documentation** – https://docs.python.org/3/library/datetime.html
- **Real Python: Python Timer Functions** – https://realpython.com/python-timer/
- **Python datetime Tutorial (Corey Schafer, YouTube)** – https://www.youtube.com/watch?v=eirjjyP2qcQ
- **Dateutil (Powerful Third-Party Extension)** – https://dateutil.readthedocs.io/
- **Pendulum (Alternative Datetime Library)** – https://pendulum.eustace.io/
