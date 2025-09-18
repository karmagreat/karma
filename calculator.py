#ask user about operation he want to use with "input()"
operation = input("Choose operation +,-,*,/: ")
#ask two value on which operation will be performed
num1=int(input("Enter first value: "))    
num2=int(input("Enter second value: "))    
#create a loop which will check operation and then it applies on values
if operation=="+":
  #write operation in "+" so python will see it as sting not a operator
    print("Ans:",num1+num2)
elif operation=="-":
    print("Ans",num1-num2)
elif operation=="*":
    print("Ans",num1*num2)    
elif operation=="/":
    print("Ans",num1/num2)    
 #if operation is not matched give error to user 
else:
    print("Invalid operation!")
    
