print("welcome to deposite and withdrawal program")
print("please select options from the following")
print("Deposite = d")
print("Deposite = w")

try:
    operator = input("enter your option : ")
    accountBalance = 1000

    if operator == "d":
        depositAmount = float(input('enter amount to be deposited: '))
        accountBalance += depositAmount
        print("Account balance = ", accountBalance)
    elif operator == "w":
        withdrawalAmount = float(input('enter amount to be withdraw: '))
        accountBalance -= withdrawalAmount
        print("Account balance = ", accountBalance)
    else:
        print("Wrong Option, enter d = Deposite OR enter w = Withdrawal")

except:
    print("error detected")