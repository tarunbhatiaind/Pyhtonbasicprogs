# # Little monk loves good string. Good String is a string that only contains vowels . Now, his teacher gave him a string S. Little monk is wondering what is the length of the longest good string which is a substring of S.

# # Note: Strings contains only lower case English Alphabets.

# # Input:
# # First line contains a string S, , where S denotes the length of the string.

# # Output:
# # Print an integer denoting the length of the longest good substring, that is substring consists of only vowels.

# # Sample input : 
# # abcaac
# # Output:
# # 2

# a = input()
# list(a)
# length = len(a)
# goodlen =[0]
# vowels = ['a','e','i','o','u']

# for i in range(length):
#   if a[i] in vowels:
#       j=i+1
#       flag = 1
#       goodlen.append(flag)
      
#       for j in range(i+1,length):
        
#           if a[j] in vowels :
#                 flag = flag + 1 
#                 goodlen.append(flag)
#           else:
#               break  
#   else:
#      continue 
# print(goodlen)        
# print(max(goodlen)) 

import re
s=input()
str=s.split('b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z')
print(str)
a=0
for i in str:
    if len(i)>a:
        a=len(i)      
print(a)