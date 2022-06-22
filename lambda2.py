li = [13, 98, 5, 62, 8, 9, 3, 38, 23, 37]

a = filter (lambda x: x % 2 == 0, li)
print(list(a))

b= map (lambda x: x % 2 == 0, li)
print(list(b))
