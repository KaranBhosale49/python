r = 5
for i in range(1, r + 1):
    for j in range(1, r + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()