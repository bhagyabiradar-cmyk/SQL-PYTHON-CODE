import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["Asha", "Rahul", "Sneha", "Arjun", "Priya", "Kiran"],
    "Attendance": [92, 78, 95, 65, 88, 72],
    "Marks": [88, 75, 92, 60, 85, 70]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

# Average attendance
print("\nAverage Attendance:")
print(df["Attendance"].mean())

# Students with attendance above 80
print("\nStudents with Attendance > 80:")
print(df[df["Attendance"] > 80])

# Highest marks
print("\nTop Student:")
print(df.loc[df["Marks"].idxmax()])

# Visualization
plt.bar(df["Student"], df["Attendance"])

plt.title("Student Attendance")
plt.xlabel("Student")
plt.ylabel("Attendance (%)")
plt.xticks(rotation=45)

plt.show()