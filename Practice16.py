def argu(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next of *argv :", arg)


argu('Hello', 'Welcome', 'to', 'Python Programing')


##########################################################################################################################
def kargu(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


kargu(first='Hello', mid='Good', last='Morning')
