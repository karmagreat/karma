#OOP + menu-driven Bank system project

class Account:
    #class name always in capital for ex: Account
    def __init__(self,name,balance=0):
    #__init__ is special method called automatically when new object is created from class
        self.name=name
        self.balance=balance
        
    def display(self):
        #function to show data we created or user stored
        print(f"Holder name: {self.name}, Balance: {self.balance}$")
        
    def deposit(self,amount):
        #fnction to deposit money in account 
        self.balance+=amount 
        #self.balance=self.balance+amount
        print(f"{amount}$ deposited, New balance: {self.balance}$")
        
    def withdraw(self,amount):
        #function for withdrawl process
        if self.balance>=amount:
            self.balance-=amount
            #self.balance=self.balance-amount
            print(f"{amount}$ debited, New balance{self.balance}$")
        else:
            print("Insuficent balance!")#if balance<amount
          
#Empty dictionary            
account={}
while True:
    choose=int(input("Select one option\n 1 Add info \n 2 Display account \n 3 Deposit \n 4 Withdraw \n 5 Exit\n 6 All acounts  \n-->"))
#Loop for menu 
#1 to add data of new account
    if choose==1:
        name=input("Enter holder's name: ")
        balance=float(input("Amount you want to add: "))
        account[name]=Account(name,balance)
        print(f"Account created for {name}\n")  
#2 to see if account is created or not
    elif choose==2:
        name=input("Holder name: \n")
        if name in account:
            account[name].display()
        else:
            print("Not found!\n")
#3 to deposit money in account    
    elif choose==3:
        name=input("Holder name: \n")
        if name in account:
            amount=int(input("Amount you want to deposit: \n"))
            account[name].deposit(amount)
        else:
            print("Not found!\n")
#4 to withsraw money    
    elif choose==4:
        name=input("Holder name: \n")
        if name in account:
            amount=int(input("AMount you want to withdraw: \n"))
            account[name].withdraw(amount)
        else:
            print("Not found!\n")
#5 to exit from loop and system    
    elif choose==5:
        print("Thank you for using our bank system. Goodbye sir/mam")
        break
""" For the system manager to see info of accounts     
    elif choose==6:
        if account:
            for acc in account.values():
                acc.display() # you can aslo use print(acc)
        else:
            print("No account created yet!")
"""  
    else:
        print("Error...\n")
