import sqlite3

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    python INTEGER,
    sql INTEGER,
    dbms INTEGER
)
""")

students = [
    (1, "Bhagyashree", 85, 90, 88),
    (2, "Rahul", 72, 80, 75),
    (3, "Anita", 95, 92, 90),
    (4, "Kiran", 65, 70, 68),
    (5, "Priya", 88, 85, 91)
]

cursor.executemany("""
INSERT OR REPLACE INTO students
(id, name, python, sql, dbms)
VALUES (?, ?, ?, ?, ?)
""", students)

conn.commit()

print("STUDENT RESULTS")
print("-" * 40)

cursor.execute("""
SELECT name,
       python,
       sql,
       dbms,
       (python + sql + dbms) AS total,
       ROUND((python + sql + dbms) / 3.0, 2) AS average
FROM students
""")

for student in cursor.fetchall():
    print(student)

print("\nStudents with average above 80:")
print("-" * 40)

cursor.execute("""
SELECT name,
       ROUND((python + sql + dbms) / 3.0, 2) AS average
FROM students
WHERE (python + sql + dbms) / 3.0 > 80
""")

for student in cursor.fetchall():
    print(student)

print("\nTop Student:")
print("-" * 40)

cursor.execute("""
SELECT name,
       (python + sql + dbms) AS total
FROM students
ORDER BY total DESC
LIMIT 1
""")

print(cursor.fetchone())

conn.close()