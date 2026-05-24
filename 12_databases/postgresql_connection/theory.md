# PostgreSQL: Scaling to Production

While SQLite is amazing for local apps, professional web applications (like the ones you'll build with Django or FastAPI) almost always use **PostgreSQL**. 

---

## 1. SQLite vs. PostgreSQL
| Feature | SQLite | PostgreSQL |
| :--- | :--- | :--- |
| **Type** | File-based | Server-based (Client-Server) |
| **Concurrency** | One writer at a time | Thousands of simultaneous users |
| **Features** | Simple, limited | Advanced (JSON support, Geo-data) |
| **Production** | Small/Medium apps | Enterprise-grade |

---

## 2. The `psycopg2` Library
To talk to PostgreSQL from Python, we use a library called `psycopg2`. 
- **Installation**: `pip install psycopg2-binary`

---

## 3. Connecting to the Server
Because PostgreSQL is a server, you need "Credentials" to log in. These are usually provided as a **Connection String**:
`postgresql://username:password@localhost:5432/database_name`

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="my_db",
    user="postgres",
    password="my_password"
)
```

---

## 4. Environment Variables (CRITICAL)
**Never** hardcode your database password in your `.py` files! If you upload that code to GitHub, anyone can find your password.
- **Solution**: Save your password in a `.env` file and read it using the `os` module.
- **Tip**: Use `pip install python-dotenv` and add `from dotenv import load_dotenv; load_dotenv()` at the top of your script to automatically load the `.env` file into your environment.

---

## 5. Differences in SQL Syntax
For the most part, the SQL is the same as SQLite, but there are some small differences:
- **Placeholders**: `psycopg2` uses `%s` instead of `?`.
- **Primary Keys**: Postgres often uses the `SERIAL` type for auto-incrementing IDs.

---

## 6. Best Practices
1. **Use Context Managers**: Use `with conn:` and `with conn.cursor() as cur:` to ensure the connection and cursor are closed properly, even if an error occurs.
2. **Handle Exceptions**: Database connections can fail (server down, wrong password). Always wrap your connection code in a `try/except` block.
3. **Closing**: Just like a file, a database connection is a "resource." If you open too many without closing them, the server will refuse to talk to you!

## Resources
- **PostgreSQL Official Documentation** – https://www.postgresql.org/docs/
- **psycopg2 Documentation** – https://www.psycopg.org/docs/
- **Real Python – How to Use PostgreSQL with Python (psycopg2)** – https://realpython.com/python-postgresql/
- **Corey Schafer – PostgreSQL & Python (psycopg2) Tutorial** – https://www.youtube.com/watch?v=qw--VYLpxG4
- **DigitalOcean – How To Connect to a PostgreSQL Database Using Python** – https://www.digitalocean.com/community/tutorials/how-to-connect-to-a-postgresql-database-using-python-and-psycopg2
- **Stack Overflow – PostgreSQL Python Questions** – https://stackoverflow.com/questions/tagged/postgresql+python
