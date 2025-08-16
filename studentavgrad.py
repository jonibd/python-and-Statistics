student = {}

n = int(input("Enter the value of n: "))
for i in range(n):
    name = input("Enter your name: ")
    marks = []
    sub = int(input("Enter number of subjects: "))
    
    for j in range(sub):
        mark = int(input("Enter your marks: "))
        marks.append(mark)
    
    student[name] = marks  

print("\nStudent Data:", student)

print("\n--- Result ---")
for name, marks in student.items():
    average = sum(marks) / len(marks)

    
    if 80 <= average <= 100:
        grade = "A+"
    elif 70 <= average < 80:
        grade = "A-"
    elif 60 <= average < 70:
        grade = "B"
    elif 50 <= average < 60:
        grade = "B-"
    else:
        grade = "Fail"
    
    print(f"{name}: Average = {average:.2f}, Grade = {grade}")
