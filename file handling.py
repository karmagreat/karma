# We have made bank accountimport json
class Account:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
        
    def display(self):
        print(f"Holder name: {self.name}, Balance: {self.balance}")    

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount}$ Deposited, New balance: {self.balance}")

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"{amount}$ debited, New balance{self.balance}")
        else:
            print("Insuficent balance!")
# File handling 
def save_account(accounts):
    with open ("account.json","w") as f:
      # with make ensures that resources are properly cleaned up after use, like closing a file automatically, even if an error occurs.
      #open helps in opening a file
      # as f file object is assign to variable f
        json.dump({name:acc.__dict__ for name,acc in accounts.items()},f,indent=4)
      #json.dump(data,f) it will let you store python data for ex: dict,list,str,etc in json file 
      #acc.__dict__ .__dict__ convert your object in dictionary beacues object itself cant be stored in file 
      #{key_expression: value_expression for item in iterable}
      # name: acc.__dict__ for name,acc in account.items()
      # By default json.dump write everything in one single long line, so we use indent=4 it will make 4 number of space to indenteach level
def load_account():
    try:
       with open("account.json","r") as f:
           data=json.load(f)
           return{name:Account(**acc) for name,acc in data.items()}
    except FileNotFoundError:
        return{}
#try: → Python will try to run the code inside this block.
#with open("account.json","r") as f: → tries to open the file.
#data = json.load(f) → reads JSON data into a Python dictionary.
#return {name: Account(**acc) for name, acc in data.items()} → converts dictionaries back into Account objects.
#If something goes wrong only if the file does not exist:
#except FileNotFoundError: → Python runs this block instead of crashing.
#return {} → returns an empty dictionary so your program can continue.
    
accounts=load_account()
#account=load_account() helps in calling load_account function
while True:
    choose=int(input("Select option \n 1 Create account \n 2 Display account \n 3 Deposit \n 4 Withdraw \n 5 exit \n"))                
    if choose==1:
        name=input("Holder's name: \n")
        balance=float(input("Amount: \n"))
        accounts[name]=Account(name,balance)
        save_account(accounts)
      #save_account(accounts) is called after every change to keep the file updated.
        print(f"Account created for {name}\n")

    elif choose==2:
        name=input("Holder's name")
        if name in accounts:
            accounts[name].display()
        else:
            print("Not found!")

    elif choose==3:
        name=input("Holder's name")
        if name in accounts:
            amount=int(input("Amount: "))
            accounts[name].deposit(amount)
        else:
            print("Not found!") 

    elif choose==4:
        name=input("Holder's name")
        if name in accounts:
             amount=int(input("Amount: "))
             accounts[name].withdraw(amount)
        else:
            print("Not found!")

    elif choose==5:
        print("Thank you for using our system...")
        break

    else:
        print("Error!!!")

