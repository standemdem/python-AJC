-- create_table.sql
CREATE TABLE IF NOT EXISTS 
    students (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER,
        grade FLOAT
    );
    
CREATE TABLE IF NOT EXISTS
    classroom (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL
    );