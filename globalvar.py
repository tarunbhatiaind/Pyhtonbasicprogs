#Global keyword

# l=5
#
# def fun1(n) :
#     #l=10 #possible because this is local variable
#     #l=l+5 #not possible because trying to change the global var therefore ,
#      global l    #to get the permission to play with global variables we use global keyword
#      l=l+5
#      print(l,n)
#
# fun1("Hello")
# print(l)

x=67
def harry():
    x=4
    def bhatia():
        global x
        x=80
    print("val of x before calling bhatia()",x)
    bhatia()
    print("val of x after calling bhatia",x)
harry()
print(x)