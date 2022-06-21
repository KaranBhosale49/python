a = int(input("Enter first number"))
b = int(input("Enter Second number"))
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5.Power\nEnter your choice:")
n=0
while n<6:
    n= int(input("enter choice"))
    if n == 1:
        print(a + b)
    elif n == 2:
        if a > b:
            print(a - b)
        else:
            print(b - a)
    elif n == 3:
        print(a * b)
    elif n == 4:
        if a > b:
            print(a / b)
        else:
            print(b / a)
    elif n == 5:
        print(a ** b)
    else:
        print("Wrong choice")