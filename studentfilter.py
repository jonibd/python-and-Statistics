student={}
n=int(input("Enter the value of student:"))
Filter_student={}
for item in range(n):
    name=input("Enter your name:")
    marks=int(input("Enter your marks:"))
    student[name]=marks

for name,mark in student.items():
    if mark>33:
        Filter_student[name]=mark
print(student)
print(Filter_student)