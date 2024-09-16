import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    # Get the connection URL from the environment variable
    database_url = os.getenv('DATABASE_URL')
    
    # Check if the DATABASE_URL is available
    if not database_url:
        raise RuntimeError('DATABASE_URL environment variable is not set.')
    
    try:
        # Establish a connection using the connection URL
        conn = psycopg2.connect(database_url)
        return conn
    except psycopg2.OperationalError as e:
        print(f"Error connecting to the database: {e}")
        raise

# Create the contacts table if it doesn't exist
def create_table():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            message TEXT,
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        cur.execute(create_table_query)
        conn.commit()
        
    except Exception as e:
        print(f"Error creating table: {e}")
        raise
    finally:
        # Ensure the cursor and connection are closed
        if cur:
            cur.close()
        if conn:
            conn.close()

# Call this function when initializing the app
if __name__ == "__main__":
    try:
        create_table()
        print("Table created successfully or already exists.")
    except Exception as e:
        print(f"Failed to create table: {e}")
