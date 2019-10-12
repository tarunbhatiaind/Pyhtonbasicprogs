var1=5
var2=6

print("enter a val")
var3=int(input())
if var3>var2:
    print("greatest")
elif var2>var3:
    print("var2 is greatest")
else:
    print("equal hain")

#in & not in keyword
l=[5,6,7]
print(15 not in l)
if 5 not in l:
    print("not in list")
else:
    print("it's in list ")

#harry quiz

print("Enter ur age")
age=int(input())

if age>18 and age<100:
    print("Eligible for voting")
elif age==18:
    print("Can't decide")
elif age>7 and age<18:
    print("not eliglible fr voting")

else:
    print("enter valid number")

a = int(input("enter a \n"))
b= int(input("enter b \n"))

if a>b: print("A is grrater")
else:print("B greater ")

c = int(input("enter c \n"))
d= int(input("enter d \n"))

print("c is biger") if c>d else print("d is greater")