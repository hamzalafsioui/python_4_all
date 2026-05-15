# ORM with SQLAlchemy: Stop Writing SQL

In the previous lessons, we wrote raw SQL strings like `"SELECT * FROM users"`. This works, but it's prone to typos and hard to manage in large projects. Professional developers use an **ORM (Object-Relational Mapper)** to talk to databases using pure Python objects.

---

## 1. What is an ORM?
An ORM is a "translator" that maps Python classes to database tables.
- **Class** = **Table**
- **Object** = **Row**
- **Attribute** = **Column**

Instead of writing SQL, you just interact with Python objects, and the ORM generates the SQL for you.

---

## 2. Why use SQLAlchemy?
SQLAlchemy is the most popular and powerful ORM in the Python ecosystem.
- **Database Agnostic**: You can switch from SQLite to PostgreSQL by changing just ONE line of code.
- **Security**: It automatically prevents SQL injection.
- **Intuitive**: It feels like writing standard Python.

---

## 3. Key Concepts

### The Engine
The "starting point" of any SQLAlchemy app. it handles the connection to the database.
```python
from sqlalchemy import create_engine
engine = create_engine("sqlite:///app.db")
```

### The Base
All your database models (classes) must inherit from a "Declarative Base".
```python
from sqlalchemy.orm import declarative_base
Base = declarative_base()
```

### The Session
The "workspace" where you do your work. You add objects to a session, and then "commit" them to save to the database.
```python
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
```

---

## 4. Defining a Model
```python
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
```

---

## 5. CRUD Operations with ORM

| Action | SQL Style | SQLAlchemy Style |
| :--- | :--- | :--- |
| **Create** | `INSERT INTO...` | `session.add(user_obj)` |
| **Read** | `SELECT * FROM...` | `session.query(User).all()` |
| **Update** | `UPDATE users...` | `user.name = "New Name"` |
| **Delete** | `DELETE FROM...` | `session.delete(user_obj)` |

---
## 5. Installation

```bash
# PowerShell
.venv\Scripts\Activate
pip install sqlalchemy
```

---
## 6. Best Practices

1. **Always Commit**: Just like raw SQL, your changes aren't permanent until you call `session.commit()`.
2. **Use Type Hints**: Modern SQLAlchemy works beautifully with Python type hints for better autocompletion.
3. **Session Management**: Always close your session when finished (`session.close()`).
