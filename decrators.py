def dec1(func1):
    def exec():
        print("executing")
        func1()
        print("executed")
    return exec

@dec1
def new_func():
    print("still in execution")

# new_func=dec1(new_func)
new_func()
