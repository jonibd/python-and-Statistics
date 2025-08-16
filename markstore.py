student = {}
n = int(input("Enter number of students: "))

# Taking input
for _ in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    student[name] = marks

# Sorting by marks (Descending)
sorted_students = sorted(student.items(), key=lambda x: x[1], reverse=True)

# Displaying result
print("\nSorted (by marks - descending):")
for name, marks in sorted_students:
    print(f"{name}: {marks}")
