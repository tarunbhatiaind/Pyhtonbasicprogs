# import time
# print(time.asctime(time.localtime(time.time())))
# lst1 = [1,1,2,3,4,5,5,8]
# lst2 = [2,3,4,5,5,6,1,3,7]
# lst3 = []
# lst4=[]
# lst3 = lst1+lst2
# for element in lst3:
#     if element not in lst4:
#         lst4.append(element)
# lst4.sort()
# print(lst4)        
# print(time.asctime(time.localtime(time.time())))


lst1 = [1,1,2,3,4,5,5,8]
lst2=[None] *len(lst1)
lst2[5]=lst1[2]
print(lst2)
