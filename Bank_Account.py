
class MyAccount:

    def __init__(self):
        self.balance = 0
        
    print("Welcome to Skill Up Bank ")

    def deposit(self):
        amount = float(input("enter CREDIT amount : "))
        self.balance += amount
        print("deposit successful", amount)

    print("")
    def withdrawal(self):
        amount = float(input("enter DEBIT amount : "))
        if self.balance >= amount:
            self.balance -= amount
            print("withdrawal successful", amount)
        else:
            print("insuffient funds")

    def accountBalance(self):
        print("account balance", self.balance)
   
    
myATM = MyAccount()

myATM.deposit() 
myATM.withdrawal()
myATM.accountBalance()
