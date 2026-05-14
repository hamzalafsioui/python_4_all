"""
EXERCISES: The Postgres Professional

Note: These exercises focus on WRITING the code correctly. 
You don't necessarily need a running server to complete the logic.

EXERCISE 1: The Connection Factory
1. Write a function 'get_connection(config_dict)' that takes a dictionary of parameters.
2. It should return a psycopg2 connection object.
3. Use a 'try/except' block to handle connection errors.

EXERCISE 2: The Secure Selector
1. Create a function 'find_user_by_email(email)'.
2. Use a 'with' block for the connection.
3. Use the '%s' placeholder to securely search for the email.
   (Hint: cur.execute("SELECT * FROM users WHERE email = %s", (email,)))

EXERCISE 3: Data Insertion
1. Write a function 'add_product(name, price)'.
2. It should insert a new product and then use 'conn.commit()' to save it.
3. Print a success message if it works.
"""

import psycopg2
from psycopg2 import Error
import os
from dotenv import load_dotenv
load_dotenv()

# TODO: Implement the exercises below

def get_connection(config_dict):
    try:
        connection = psycopg2.connect(**config_dict)
        return connection
    except Error as e:
        print(f"Error while connecting to PostgreSQL: {e}")
        return None

def find_user_by_email(config,email):
    with get_connection(config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE email = %s", (email,))
            return cur.fetchone()

def add_product(config,name, price):
    with get_connection(config) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (name, price))
            conn.commit()
            print("Product added successfully")

if __name__ == "__main__":
   # We read from environment variables for security Make sure Credentials are correct in .env file
   db_user = os.getenv("DB_USER", "postgres")
   db_password = os.getenv("DB_PASSWORD")
   db_host = os.getenv("DB_HOST", "127.0.0.1")
   db_port = os.getenv("DB_PORT", "5432")
   db_name = os.getenv("DB_NAME", "test_db")
        
   config = {"user": db_user, "password": db_password, "host": db_host, "port": db_port, "dbname": db_name}
   print(get_connection(config))
   print(find_user_by_email(config,"hamzalafsioui@gmail.com"))
   # add_product("test_product", 100)
