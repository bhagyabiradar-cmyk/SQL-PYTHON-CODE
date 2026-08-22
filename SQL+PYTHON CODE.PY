students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Anu", "marks": 92},
    {"name": "Priya", "marks": 78},
    {"name": "Ravi", "marks": 65},
    {"name": "Sneha", "marks": 95}
]

# Students with marks > 80
for student in students:
    if student["marks"] > 80:
        print(student["name"], student["marks"])

# Average marks
total = sum(student["marks"] for student in students)
average = total / len(students)

print("Average:", average)