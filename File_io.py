# File IO basics
# RAM IMG MP3 --BINARY--ENCODE--FILE--DECODE BY SOFT
# MODES :
# r --open file --default
# w --write mode
# x --create file if not exist , faail if file exist
#a =--append--add more to file
#t --text mode --txt files --default
#b --binary mode
#+ --update file (read+write)


###########################################

f=open("tarun.txt","rt")
# print(f.readlines()) #stores and prints in list format in list
content = f.read()
print(content)
a=f.write('Tarun has moved ot Germany')
print()
# for line in f:
#     print(line) #print line by line

# print(f.readline()) 
#f.close() #close is necessary practice because some one may also be usding the file

# content = f.read(344)
# print(content)
f.close()