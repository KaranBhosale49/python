def triangle(a):
    k = a - 1
    for i in range(0, a):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
n = 5
triangle(n)