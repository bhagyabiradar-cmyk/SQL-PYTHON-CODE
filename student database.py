import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER,
    branch TEXT
)
""")

# Insert students
students = [
    (1, "Bhagya", 88, "ECE"),
    (2, "Rahul", 76, "CSE"),
    (3, "Anu", 92, "ECE"),
    (4, "Kiran", 69, "ISE"),
    (5, "Sneha", 85, "CSE")
]

cursor.executemany(
    "INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?)",
    students
)

# Display all students
print("\n--- All Students ---")
cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

# Students scoring above 80
print("\n--- Students Above 80 ---")
cursor.execute("""
SELECT name, marks
FROM students
WHERE marks > 80
ORDER BY marks DESC
""")

for row in cursor.fetchall():
    print(row)

# Average marks
cursor.execute("SELECT AVG(marks) FROM students")
average = cursor.fetchone()[0]

print("\nAverage Marks:", round(average, 2))

# Highest scorer
cursor.execute("""
SELECT name, marks
FROM students
ORDER BY marks DESC
LIMIT 1
""")

topper = cursor.fetchone()
print("Topper:", topper[0], "-", topper[1])

# Close connection
conn.commit()
conn.close()

print("\nDatabase operation completed!")