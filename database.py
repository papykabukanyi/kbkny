import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    # Get the connection URL from the environment variable
    database_url = os.getenv('DATABASE_URL')

    # Establish a connection using the connection URL
    conn = psycopg2.connect(database_url)
    return conn

# Create the contacts table if it doesn't exist
def create_table():
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

    cur.close()
    conn.close()

# Call this function when initializing the app
create_table()
