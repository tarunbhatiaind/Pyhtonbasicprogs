#args and kwargs

#Actual way :
# def func1 (a,b,c,d):
#     print(a,b,c,d)
#
# func1("A","b","c","d")

#args:
def func2(*args): #can use any name not only args
    print(args[1])
    for item in args:
        print(item,end="")

itm=["A","B","C","D"]
func2(*itm)

#works fine with one argument at first place and list in second
def func3(normal,*args):
    print(normal)
    for item in args:
        print(item, end="")
itm1=["d","e"]
func3('abc',*itm1)

#Below wont work because the list or combined arguments shoiuld not come in first place
# def func4(*args,normal):
# #     print(normal)
# #     for item in args:
# #         print(item, end="")
# # itm2=["d","e"]
# # func4(*itm2,'abc')
def func4(normal,*args, **kwargs): #kwargs take dictionary as input
    print(normal)
    for item in args:
        print(item)
    for key,value in kwargs.items():
         print(f"The {key} is {value}")
itm1=["d","e"]
itm2={"Tarun":"name","bhatia":"surname"}
func4('abc',*itm1,**itm2)
