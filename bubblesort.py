def bublesort(ar):
    n = len(ar)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ar[j] > ar[j + 1]:
                ar[j], ar[j + 1] = ar[j + 1], ar[j]


arr = [96, 25, 29, 7, 48, 71, 90]
bublesort(arr)
print("Sorted array is ")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
