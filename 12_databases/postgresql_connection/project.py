"""
PROJECT: The Database Health Checker

Goal: Build a utility script that verifies if a PostgreSQL database is ready for production.

Requirements:

1. Setup:
   - Create a configuration dictionary (host, dbname, user, password).
   - Use 'os.environ' to simulate secure password storage.

2. The Health Check Function:
   - Try to connect to the database.
   - If successful, check the database version using 'SELECT version()'.
   - Check if a specific table (e.g., 'system_logs') exists.
   - If it doesn't exist, create it.
   - Insert a "Health Check" timestamp into the table.

3. Error Handling:
   - If the password is wrong, print a specific error message.
   - If the host is unreachable, print a specific timeout message.

4. Cleanup:
   - Ensure the connection is closed even if the script fails.

Real-World Logic:
- Professional dev-ops engineers use scripts like this to "warm up" or verify databases before a web application starts up in a Docker container (like Kubernetes or AWS).
"""

import psycopg2
from psycopg2 import OperationalError, Error
import os
import datetime


def get_connection(config_dict):
    """
    Attempts to connect to the PostgreSQL database.
    Returns a connection object if successful, None otherwise.
    """

    try:
        conn = psycopg2.connect(
            **config_dict,
            connect_timeout=5  # Prevent hanging forever
        )

        print("Database connection successful.")
        return conn

    except OperationalError as e:
        error_message = str(e).lower()

        # Wrong password / authentication failure
        if "password authentication failed" in error_message:
            print("ERROR: Invalid database username or password.")

        # Host unreachable / timeout
        elif (
            "could not connect to server" in error_message
            or "timeout expired" in error_message
            or "connection timed out" in error_message
        ):
            print("ERROR: Database host is unreachable or timed out.")

        else:
            print(f"Operational Error: {e}")

        return None

    except Error as e:
        print(f"Database Error: {e}")
        return None


def health_check(config_dict):
    """
    Performs a health check on the database.

    Steps:
    1. Connect to PostgreSQL
    2. Check PostgreSQL version
    3. Verify 'system_logs' table exists
    4. Create table if missing
    5. Insert health-check log entry
    """

    conn = None

    try:
        conn = get_connection(config_dict)

        if conn is None:
            return

        with conn.cursor() as cur:

            # -------------------------------------------------
            # Check PostgreSQL Version
            # -------------------------------------------------
            cur.execute("SELECT version();")
            version = cur.fetchone()

            print("\n=== DATABASE VERSION ===")
            print(version[0])

            # -------------------------------------------------
            # Check if 'system_logs' table exists
            # -------------------------------------------------
            cur.execute("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables
                    WHERE table_name = 'system_logs'
                );
            """)

            table_exists = cur.fetchone()[0]

            # -------------------------------------------------
            # Create table if missing
            # -------------------------------------------------
            if not table_exists:
                print("\n'system_logs' table not found.")
                print("Creating table...")

                cur.execute("""
                    CREATE TABLE system_logs (
                        id SERIAL PRIMARY KEY,
                        log_type VARCHAR(50),
                        message TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)

                conn.commit()

                print("'system_logs' table created successfully.")

            else:
                print("\n'system_logs' table already exists.")

            # -------------------------------------------------
            # Insert Health Check Record
            # -------------------------------------------------
            timestamp = datetime.datetime.now()

            cur.execute("""
                INSERT INTO system_logs (log_type, message)
                VALUES (%s, %s);
            """, (
                "HEALTH_CHECK",
                f"System check completed at {timestamp}"
            ))

            conn.commit()

            print("Health check log inserted successfully.")

            print("\nDatabase health check PASSED.")

    except Error as e:
        print(f"Health Check Error: {e}")

    finally:
        # -------------------------------------------------
        # Cleanup
        # -------------------------------------------------
        if conn is not None:
            conn.close()
            print("Database connection closed.")


if __name__ == "__main__":

    # -------------------------------------------------
    # Environment Variables (Simulated Secure Storage)
    # -------------------------------------------------
    #
    # Linux/Mac:
    # export DB_PASSWORD=mysecretpassword
    #
    # Windows PowerShell:
    # $env:DB_PASSWORD="mysecretpassword"
    # $env:DB_NAME=test_db
    # $env:DB_HOST=127.0.0.1
    # $env:DB_PORT=5432
    # 
    # In This Project we don't use .env load_dotenv() we inject it in the code by the terminal
    # os.getenv() command in the terminal or PowerShell
    # 
    # -------------------------------------------------

    db_user = os.getenv("DB_USER", "postgres")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST", "127.0.0.1")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "test_db")

    config = {
        "user": db_user,
        "password": db_password,
        "host": db_host,
        "port": db_port,
        "dbname": db_name
    }

    health_check(config)
   
