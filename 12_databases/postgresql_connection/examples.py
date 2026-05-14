# Examples: Connecting to a Production Database

from dotenv import load_dotenv
load_dotenv()
import psycopg2
from psycopg2 import Error
import os

# --- Note on Installation ---
# active the env first .venv\Scripts\Activate
# You must run: pip install psycopg2-binary or python -m pip install psycopg2-binary

# You must run: pip install python-dotenv


def connect_to_postgres():
    """
    Demonstrates how to connect to a PostgreSQL database.
    Note: This will only work if you have a PostgreSQL server running!
    """
    try:
        # We read from environment variables for security Make sure Credentials are correct in .env file
        db_user = os.getenv("DB_USER", "postgres")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST", "127.0.0.1")
        db_port = os.getenv("DB_PORT", "5432")
        db_name = os.getenv("DB_NAME", "test_db")
        
        # Connection parameters
        connection = psycopg2.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_name
        )

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        
        # Print PostgreSQL details
        print("PostgreSQL connection is open")
        print(connection.get_dsn_parameters(), "\n")

        # Execute a simple query
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# --- Why use context managers? ---

def secure_query_demo():
    """
    The professional way to handle connections using 'with' blocks.
    """
    try:
        # The 'with' block automatically commits or rolls back
        with psycopg2.connect(database="test_db", user="postgres") as conn:
            # The second 'with' block automatically closes the cursor
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users LIMIT 5;")
                print(cur.fetchall())
                
    except Error as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    print("This example requires a live PostgreSQL server to run.")
    connect_to_postgres()
