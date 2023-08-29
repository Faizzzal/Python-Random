def myfunc(func):
    def myinnerfunc():
        print("This is inner function")
        func()
    return myinnerfunc
    

@myfunc
def myfunc2():
     print("This is my second function")
myfunc2()