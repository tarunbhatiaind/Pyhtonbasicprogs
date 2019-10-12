# #pattern print
# input : int n
# boolean = 0,1 (true , false)
# if true:
# *
# **
# ***
# else : opposite
a=1
c=1
print("Insert a number")
n=int(input())
print("Insert a boolean val 0 or 1 ")
b=int(input())
print(b)
d=n
if(b==1):
    while(a<=n):
        while(c<=a):
            print("*",end="")
            c=c+1
        print("\n")
        a=a+1
        c=1
else:
        #print("yaha aagya")
        while(n>=1):
            while(d>=1):
                print("*",end="")
                d=d-1
            print("\n")
            n=n-1
            d=n
#print(b)


