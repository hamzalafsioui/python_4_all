# SQLite Basics: Persistent Data Storage

Up until now, all the data our programs handled (lists, dictionaries, classes) disappeared as soon as the script finished running. To build real-world apps like Instagram, Amazon, or a simple Todo list, we need a way to save data permanently. We use **Databases** for this.

---

## 1. What is SQLite?
SQLite is a professional, high-performance database engine that is **built directly into Python**.
- **No Setup**: You don't need to install a server (like MySQL or Postgres).
- **File-based**: The entire database is just one file on your computer (e.g., `app.db`).
- **Standard SQL**: It uses the same language as the world's biggest database systems.

---

## 2. Basic Workflow
To use a database in Python, we follow these 4 steps:
1. **Connect**: `conn = sqlite3.connect("my_data.db")`
2. **Cursor**: Create a "cursor" to execute commands: `cursor = conn.cursor()`
3. **Execute**: Send SQL commands: `cursor.execute("CREATE TABLE...")`
4. **Commit & Close**: Save your changes and close the door: `conn.commit(); conn.close()`

---

## 3. The 4 Main Commands (CRUD)
CRUD stands for Create, Read, Update, Delete.

| Action | SQL Command | Example |
| :--- | :--- | :--- |
| **Create** | `INSERT` | `INSERT INTO users (name) VALUES ('Hamza')` |
| **Read** | `SELECT` | `SELECT * FROM users WHERE id = 1` |
| **Update** | `UPDATE` | `UPDATE users SET name = 'Ali' WHERE id = 1` |
| **Delete** | `DELETE` | `DELETE FROM users WHERE id = 1` |

---

## 4. SQL Data Types
When you create a table, you must tell SQLite what kind of data each column will hold:
- **`INTEGER`**: Whole numbers.
- **`TEXT`**: Strings.
- **`REAL`**: Decimal numbers (floats).
- **`NULL`**: Empty values.

---

## 5. Security Note: SQL Injection
Never use f-strings or `.format()` to build SQL queries with user input!
- **Wrong**: `cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")`
- **Right**: `cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))`
Using the `?` placeholder prevents hackers from "injecting" malicious code into your database.

---

## 6. Best Practices
1. **Always Commit**: If you don't call `conn.commit()`, your `INSERT` or `UPDATE` commands will be forgotten!
2. **Use Primary Keys**: Every table should have an `id INTEGER PRIMARY KEY` column to uniquely identify each row.
3. **Close Connections**: Always close your connection when finished to avoid file locking issues.

## Resources
- **SQLite Official Documentation** – https://www.sqlite.org/docs.html
- **Python Docs – sqlite3 Module** – https://docs.python.org/3/library/sqlite3.html
- **Real Python – Using SQLite with Python** – https://realpython.com/python-sqlite-sqlite3/
- **Corey Schafer – SQLite Tutorial (Python)** – https://www.youtube.com/watch?v=pd-0G0MigNU
- **GeeksforGeeks – SQLite in Python** – https://www.geeksforgeeks.org/sqlite-in-python/
- **Stack Overflow – SQLite Python Questions** – https://stackoverflow.com/questions/tagged/sqlite+python
