import sqlalchemy as sa
from dotenv import load_dotenv
import os
import urllib

# table setup queries
sql_init = [
    "DROP TABLE IF EXISTS students",
    """
    CREATE TABLE students (
        student_id SERIAL PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        enrollment_date DATE
    )
    """,
    """
    INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
        ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
        ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
    """
]

def initialize_database():
    # applies the initial database schema setup and populates it with the initial data
    
    # get db details
    load_dotenv()
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")

    try:
        # replaces special characters with url equivalent
        db_user_enc = urllib.parse.quote_plus(db_user)
        db_password_enc = urllib.parse.quote_plus(db_password)

        # connect to db
        conn_string = f"postgresql+psycopg2://{db_user_enc}:{db_password_enc}@{db_host}:{db_port}/{db_name}"
        engine = sa.create_engine(conn_string)


        with engine.begin() as conn:
            for stmt in sql_init:
                conn.execute(sa.text(stmt.strip()))

        conn.close()

        print("Database generated and populated successfully with initial data")

    except Exception as e:
        print(f"Error initializing database: {e}")


if __name__ == '__main__':
    initialize_database()
