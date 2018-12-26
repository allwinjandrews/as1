# Program to store and display details of 3 students
student_list = []

# Loop for entering details of 3 students
for i in range(3):
    rno = input('enter roll.no')
    name = input('enter name')
    std = input('enter class')
    student = {"rno": rno, "name": name, "std": std}
    student_list.append(student)

# Loop for displaying details of 3 students
for i in range(3):
    print("student", i+1, ":")
    print("Roll.no:", student_list[i]["rno"])
    print("Name:", student_list[i]["name"])
    print("Class:", student_list[i]["std"], "\n")
