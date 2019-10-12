list1=["abc","bcd","cde","fgh"]

for item in list1:
    print(item)

list2=[["Harry",2],["Tarun",4],["abc",8]]

dict2=dict(list2)
for item,count in dict2.items():
    print(item ,count)

#quiz
list3=["abc",6,"bcd",45,54]
for item in list3:
   #print(type(item))
   if type(item)== int and item>6:
       print(item)



  #""" if type(item)=="<class 'int'>"and item>6:
   #     print(item)
#print(list3) """