student_attendance=[
    ("sunday",["jony","fari","sajid"]),
    ("monday",["jamal","fari"]),
    ("tuesday",["jony","sajid"]),
    ("wednesday",["sajid","fari"]),
    ("Thursday", ["Jony", "Sami"]),
    ("Friday", ["Rafi", "Sami"])
]
v
count_attendance = {}

for day,students in student_attendance:
    # print(day)
    # print(students)

    for student in students:
        student_lower = student.lower()

        if student_lower in count_attendance:
            count_attendance[student_lower]+=1
        else:
            count_attendance[student_lower]=1
for student,count in count_attendance.items():
    print(f"{student} attended {count} days")
  
    