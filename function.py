"""
a=9
b=4
c =sum((a,b))
print(c)
"""
#user defined functions
def func1(a,b):
    print("Hello funct1",a+b)
print(func1(2,5))
func1(6,5)

def funct2(a,b):
    """This returns avg of 2 numbers"""
    # ABOVE LINE IS DOCSTRING
    average= (a+b)/2
    #print("avg of 2 num is:",average)
    return average
v=funct2(5,6) #this will not return None
print(v)

print(funct2.__doc__)   # ths will print docstring