import json
class Student:
    def __init__(self,name,student_id,course,year=1):
        self.name=name
        self.student_id=student_id
        self.course=course
        self.year=year
    
    def __str__(self):
        return f"Student: {self.name}, Id: {self.student_id}, Course: {self.course}, Year: {self.year}"

def save_data(students):
    data=[stu.__dict__ for stu in students]
    with open("students.json","w")as f:
        json.dump(data,f,indent=4)
def load_student():
    try:
        with open("students.json","r")as f:
            data=json.load(f)
            return[Student(**stu) for stu in data]        
    except FileNotFoundError:
        return[]
        #[] because we are working with list this time
class Classroom:
    def __init__(self):
        self.students=[]

    def add_student(self,student):
        self.students.append(student)     

    def view_data(self):
        if not self.students:
            print("Not available!")
        else:
            for s in self.students:
                print(s)    
    def next_year(self):
        for s in self.students:
            s.year+=1
            print(f"{s.name} promoted in year {s.year}")

classroom=Classroom()
classroom.students=load_student()
while True:
    choose=int(input("Select option \n 1 Add student \n 2 View data \n 3 next year \n 4 Exit \n")) 
    if choose==1:
        name=input("Enter name: ")
        student_id=int(input("Enter id no: "))
        course=input("Enter your course: ")
        year_input=(input("Enter year(press enter for 1st year): "))
        if year_input.strip()=="":
            student=Student(name,student_id,course)
        else:
            student=Student(name,student_id,course,int(year_input))    
        classroom.add_student(student)
        save_data(classroom.students)
    elif choose==2:
        classroom.view_data()
    elif choose==3:
        classroom.next_year()
    elif choose==4:
        print("Thank you using Snaver's system...")
        break
    else:
        print("Not defined!")    
