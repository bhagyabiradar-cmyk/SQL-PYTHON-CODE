import sqlite3

# Connect to database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")

# Insert data
employees = [
    (1, "Rahul", "IT", 60000),
    (2, "Priya", "HR", 45000),
    (3, "Amit", "IT", 75000),
    (4, "Sneha", "Finance", 65000),
    (5, "Kiran", "IT", 55000)
]

cursor.executemany(
    "INSERT OR IGNORE INTO employees VALUES (?, ?, ?, ?)",
    employees
)

# Display all employees
print("All Employees:")
cursor.execute("SELECT * FROM employees")

for row in cursor.fetchall():
    print(row)

# Find employees with salary above 60000
print("\nSalary Above 60000:")
cursor.execute("""
SELECT name, department, salary
FROM employees
WHERE salary > 60000
""")

for row in cursor.fetchall():
    print(row)

# Find average salary
cursor.execute("SELECT AVG(salary) FROM employees")
average = cursor.fetchone()[0]

print("\nAverage Salary:", average)

# Find highest salary
cursor.execute("SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 1")
highest = cursor.fetchone()

print("Highest Salary:", highest)

conn.commit()
conn.close()