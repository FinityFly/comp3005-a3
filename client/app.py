import sqlalchemy as sa
from dotenv import load_dotenv
import os
import urllib
from init import initialize_database

# get db conn details
load_dotenv()
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

# replaces special characters with url equivalent
db_user_enc = urllib.parse.quote_plus(db_user)
db_password_enc = urllib.parse.quote_plus(db_password)

# connect to db
conn_string = f"postgresql+psycopg2://{db_user_enc}:{db_password_enc}@{db_host}:{db_port}/{db_name}"
engine = sa.create_engine(conn_string)

def getAllStudents():
    # retrieves and displays all records from the students table
    with engine.connect() as conn:
        try:
            result = conn.execute(sa.text("SELECT * FROM students;"))
            students = result.fetchall()
            print("Students:")
            for student in students:
                print(student)
        except Exception as e:
            print(f"Error getting students: {e}")

def addStudent(first_name, last_name, email, enrollment_date):
    # inserts a new student record into the students table
    # use a transaction so the insert is committed
    try:
        with engine.begin() as conn:
            stmt = sa.text("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (:fn, :ln, :em, :ed);")
            conn.execute(stmt, {"fn": first_name, "ln": last_name, "em": email, "ed": enrollment_date})
        print(f"Student {first_name} {last_name} added successfully")
    except Exception as e:
        print(f"Error adding student: {e}")

def updateStudentEmail(student_id, email):
    # updates the email address for a student with the specified student_id
    try:
        with engine.begin() as conn:
            stmt = sa.text("UPDATE students SET email = :e WHERE student_id = :sid;")
            result = conn.execute(stmt, {"e": email, "sid": student_id})
        if result.rowcount > 0:
            print(f"Email for student {student_id} updated successfully")
        else:
            print(f"Student with ID {student_id} not found")
    except Exception as e:
        print(f"Error updating email: {e}")

def deleteStudent(student_id):
    # deletes the record of the student with the specified student_id
    try:
        with engine.begin() as conn:
            stmt = sa.text("DELETE FROM students WHERE student_id = :sid;")
            result = conn.execute(stmt, {"sid": student_id})
        if result.rowcount > 0:
            print(f"Student {student_id} deleted successfully")
        else:
            print(f"Student with ID {student_id} not found")
    except Exception as e:
        print(f"Error deleting student: {e}")

if __name__ == '__main__':
    # initialize the database
    print("--- Initialize database ---")
    initialize_database()

    # goes through all of the database operations
    print("--- Getting all students ---")
    getAllStudents()

    print("\n--- Adding new students (adding Jimmy Butler and Lebron James) ---")
    new_students = [
        ['Jimmy', 'Butler', 'buckets@warriors.com', '2023-09-03'],
        ['LeBron', 'James', 'goat@lakers.com', '2023-09-04']
    ]
    for student in new_students:
        addStudent(student[0], student[1], student[2], student[3])
    getAllStudents()

    print("\n--- Updating student's email (updating email for student 4) ---")
    updateStudentEmail(4, 'jimmy@warriors.com')
    getAllStudents()

    print("\n--- Deleting a student (deleting student 2) ---")
    deleteStudent(2)
    getAllStudents()
