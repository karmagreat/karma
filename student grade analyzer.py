# ask user for total student
num_student=int(input("enter total student: "))
# empty list where student's data will be stored
student=[]
# collecting student name & marks and appending in empty list
for i in range(num_student): #range will make sure loop runs upto value of num_student 
    student_name=str(input("enter student name: "))
    marks=float(input("enter marks: "))
    student.append((student_name,marks))
print()
print(student)    
# Finding avg marks
total=0
for name,marks in student:
    total +=marks
avg=total/len(student)
print("Avg marks: ",avg)
print()
#finding Highest and Lowest marks
highest=max(student, key=lambda x: x[1])    
lowest=min(student,key=lambda x: x[1])
print("Highest marks:",highest)
print("Lowest marks:",lowest)    
