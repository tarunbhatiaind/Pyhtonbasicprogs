#=============insert in file some data ============================
# f=open("file.txt","r+")
# f.write("Tarun ")
# f.write("\nis a nice")
# f.write("\nBoy")
# f.close()
#------------------tell()----------------------------------
# f=open("file.txt","r")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.close())

#=======================seek()=====================================

f=open("file.txt","r")
print(f.readline())
f.seek(9) #tell the file pointer place
print(f.readline())
print(f.close())

#======================================================================