lst=[]
num = int(input('no of inputs'))
for i in range(num):
    str =input()
    lst.append(str)
for i in range(num):
  str1 = ''.join(reversed(lst[i]))
  if lst[i] == str1:
    if(len(str1)%2==0):
            print("YES EVEN")
    else:
            print("YES ODD")
  else:
    print("NO")