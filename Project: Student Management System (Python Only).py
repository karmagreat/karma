#create empty dic for name of student and marks
student={}

#create a function for adding student data (name/marks)
def add_student(): #def in python stands for define 
#             How function work
# Define Function_Name (Argument):
    student_name=input("Enter student name: ")
    # collecting input
    marks=float(input("Enter marks of student: "))
    student[student_name]=marks
    print(f"student: {student_name} added succesfully")
    
# Create a function which will let us see data we stored    
def view_data():
    if not student: 
# Not is logical operator which flip meanings TRUE = False and FALSE = TRUE
        print("Nothing available!") #if dic is empty 
    else:
        print("Data available..")
        
# create a function for finding average marks         
def average_marks():
    if not student:
        print("Not available!")
    else:
        avg=sum(student.values())/len(student)
        #avg formula sum of marks/total student
        print("class Average marks:",avg)
        
# Create function for finding highest marks
def highest_lowest():
    highest=max(student,key=student.get)
    lowest=min(student,key=student.get)    
    print("Highest marks:",highest,student[highest])
    print("Lowest marks:",lowest,student[lowest])    
#we used .get because we are using dic and with dictionary we use .get not lambda x: x[1]


#create a loop which will let user to call any function how many times he/she want
while True:
    choose=int(input("select what u want to do: \n 1 Add_student\n 2 View_data \n 3 Average_marks \n 4 Highest_lowest \n 5 Exit \n"))
    if choose==1:
        add_student()
    elif choose==2:
        view_data()
    elif choose==3:
        average_marks()
    elif choose==4:
        highest_lowest()
    elif choose==5:
        break #stop the loop
    else:
        print("Invalid input!")
