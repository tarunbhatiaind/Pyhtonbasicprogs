# # Factorial using recurssion
# def factorial(n):
#    if n ==1:
#        return  1
#    else:
#        return n*factorial(n-1)
# #while
# #num=int(input("enter a no"))
# def facint(num):
#
#     i=1
#     fact=1
#     while(i<=num):
#          fact=fact*i
#          i=i+1
#     return fact
# #using for
#
# # num=int(input("enter a no"))
# #
# def factf(num):
#     fact=1
#     for i in range(num):
#          fact=fact*(i+1)
#     return fact
#
#
# b=facint(5)
# a=factorial(5)
# c=factf(5)
# print(a)
# print(b)
# print(c)

def fib(n):
    my_list=[]
    my_list.append(0)
    my_list.append(1)
    i=2
    while(i<=n-1):

        k=my_list[i-1]+my_list[i-2]
        my_list.append(k)
        i=i+1
    print(my_list)
a=int(input("Enter the length of series you want ?\n"))
fib(a)

def fibonaki(n):

    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonaki(n-1)+fibonaki(n-2)
k=fibonaki(5)
print(k)