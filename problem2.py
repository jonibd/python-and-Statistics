student={

}
n=int(input("Enter your subject number :"))
for x in range(n):
    subject=input("Enter your subject :")
    marks=int(input("Enter your marks :"))
    student[subject]=marks

print(student)

hiest_subject=""
hiest_marks=-1

for sub, mark in student.items():
    if mark>hiest_marks:
        hiest_marks=mark
        hiest_subject=sub

print(f"\nhiest marks {hiest_subject} in marks{hiest_marks}.")


