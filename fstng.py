import math
# Normal way of string formatting (Complicated)
me ="tARUN"
b="good"
a="tHIS IS %s %s"%(me ,b)
print(a)

#One more way(complicated again)

g="This is {0} {1}"
c=g.format(me,b)
print(c)
#FSTRINGS:

x=f"This is {me} {b}" #Using f in the begining
print(x)

h= f"This is {me} {b} {56*9} {math.sin(90)}"
print(h)