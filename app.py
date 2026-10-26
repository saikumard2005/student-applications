
from flask import Flask
import sqlite3

app = Flask(__name__)

# Create database and student table
def create_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            marks INTEGER NOT NULL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO students (id, name, course, marks) VALUES (?, ?, ?, ?)",
            [
                (1, "Sai Kumar", "CSE", 85),
                (2, "Rahul", "ECE", 90),
                (3, "Priya", "CSE", 88)
            ]
        )

    conn.commit()
    conn.close()


# Retrieve student information
@app.route("/")
def display_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, course, marks FROM students")
    students = cursor.fetchall()

    conn.close()

    html = """
    <h1>Student Information</h1>
    <table border="1" cellpadding="10">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Course</th>
            <th>Marks</th>
        </tr>
    """

    for student in students:
        html += f"""
        <tr>
            <td>{student[0]}</td>
            <td>{student[1]}</td>
            <td>{student[2]}</td>
            <td>{student[3]}</td>
        </tr>
        """

    html += "</table>"
    return html


if __name__ == "__main__":
    create_database()
    app.run(debug=True)
