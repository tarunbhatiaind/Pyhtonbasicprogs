itms = ["Abc","bcd","cde","def" ]

# Traditional way :

# i=0
# for item in itms:
#     if i%2==0:
#         print(item)
#     i+=1
for index,item in enumerate(itms):
      if index%2==0:
          print(f"items needed are {item}")
