class bank_account():

    def __init__(self) -> None:
        self.amount = 0

    def deposite(self, Amount):
        self.amount += Amount
        print("deposite successful")

    def withdraw(self, Amount):
        if self.amount >= Amount:
            self.amount -= Amount
            print("withdrawal successful")
        else:
            print("insuffient funds")

    def display(self):
        print("balance : ", self.amount)


atm = bank_account()

for i in range(0, 50):

    print("1 = deposit, 2 = withdrawal, 3 = display, 4 = exit")
    option = int(input("enter option : "))

    if option == 1:
        Amount = float(input("enter Amount : "))
        atm.deposite(Amount)
    elif option == 2:
        Amount = float(input("enter Amount : "))
        atm.withdraw(Amount)
    elif option == 3:
        atm.display()
    elif option == 4:
        exit()
    else:
        print("enter the right option")
