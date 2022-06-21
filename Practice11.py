

number = int(input("Enter the number to Reverse : "))
reverse = 0
while (number > 0):
    temp = number % 10
    reverse = reverse * 10 + temp
    number = number // 10
    print(number)
print("The Reversed Number is: ", reverse)