# COMP3005 Assignment 3

```
Student: Daniel Lu
Student Number: 101304181
Fall 2025 - Abdelghny Orogat
```

## Getting Started

### Setup

- **PostgreSQL prerequisite**
    - Ensure you have the PostgreSQL installed
    - Create a new database for this project via the SQL command `CREATE DATABASE new_db;`
    - Note down the database connection details in the "Properties" tab
- **Python application setup**
    - Install the required packages via `pip install -r requirements.txt`
    - Create a `.env` file that contains your database connection details in this format:
```bash
DB_NAME="your_database_name"
DB_USER="your_username"
DB_PASSWORD="your_password"
DB_HOST="localhost"
DB_PORT="5432"
```

### Running the Application

To create the `students` table and populate it with data, we must run init.py:
```bash
python client/init.py
```
Our database should now have a properly initialized `students` table with our initial data.

---

To run our operations, run app.py:
```bash
python client/app.py
```

The script will perform the following operations:
1.  Display all students
2.  Add a new student
3.  Update a student's email
4.  Delete a student