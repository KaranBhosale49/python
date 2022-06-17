def addd(a,*b):
    a+=sum(b)
    return a
print(addd(10,3,2,4,6))