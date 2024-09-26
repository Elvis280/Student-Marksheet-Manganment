# Marksheet Management System

## Overview

The Marksheet Management System is a Python-based application that allows users to manage student records, including adding, updating, deleting, and searching for student information. The system interacts with a MySQL database to store and retrieve data efficiently.

## Features

- Add Student Record: Add a new student along with their marks in various subjects.
- Search Student Record: Search for student records by name.
- Update Student Marks: Update the marks of existing students in specified subjects.
- Delete Student Record: Delete a student record using their roll number.
- Display All Records: View all student records stored in the database.

## Technologies Used

- Programming Language: Python
- Database: MySQL
- Libraries: mysql-connector-python

## Make sure you have MySQL installed and running on your system.

- Create a database named school.
- Create a table named student with the following schema:
CREATE TABLE student (
    roll_no INT PRIMARY KEY,
    name VARCHAR(100),
    english INT,
    physics INT,
    chemistry INT,
    maths INT,
    cs INT
  );

## Also
-You may need to install the MySQL connector library if you haven't already:

pip install mysql-connector-python
