import sqlite3

# Connect to the database or create a new one if it doesn't exist
conn = sqlite3.connect('class.db')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create the first table called "students"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER,
        grade FLOAT
    )
''')

cursor.execute('''
    INSERT INTO  students (first_name, last_name, age, mean)
    VALUES (student.first_name, )
    )
''')
# Commit the changes and close the connection
conn.commit()
conn.close()
