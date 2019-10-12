"""""
print("A","\nB")
"""
print("Enter the operation you want to do :")
print("type 1 for addition")
print("type 2 for subtraction")
print("type 3 for multiplication")
print("Type 4 for division")
op=int(input())
if op == 1 or op == 2 or op == 3 or op == 4:
    print("Enter the 2 numbers for the operations :")
a=int(input())
b=int(input())
if op==3:
    if a==45 and b==3 or a==3 and b==45:
        print("Ans is :555")
    else:
        print("ans is :",a*b)
if op==2:
    print("ans is ",a-b)
if op==1:
    if a==56 and b==9 or a==9 and b==56:
        print("ans is : 77")
    else:
        print("ans is",a+b)
if op==4:
    if a==56 and b==6:
        print("Answer is: 4.0")
    else:
        print("answer is:",a/b)
else:
       print("invalid input")
