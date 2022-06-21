balance = 1000
n=0
print("Welcome to ATM Machine")
while n<4:
    print("Select Transaction")
    print("1: BALANCE\n2: WITHDRAW\n3: DEPOSIT\n4: EXIT")
    n = int(input("Enter Transaction "))
    if(n == 1):
        print("Your balance is ", balance)
    elif(n==2):
        withdraw = int(input("Enter amount to withdraw "))
        if(balance > withdraw):
            balance -= withdraw
            print("success")
            print("account balance",balance)
        else:
            print("insufficient Balance")
    elif(n==3):
        deposit = int(input("Enter amount to deposit "))
        balance += deposit
        print("success")
        print("account balance ", balance)
    elif(n==4):
        exit()
    else:
        print("no selected transaction")