with open("file.txt") as f :
     a=f.readline()
     print(a)
     print(f.tell())
#---below code will work even if i use the same file pointer reason is block automatically closed the file after use and rest below code is new
f=open("file.txt")
print(f.tell())
a=f.readline()
print(a)
f.close()