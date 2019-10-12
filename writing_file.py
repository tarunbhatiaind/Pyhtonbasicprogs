# f=open("tarun2.txt","a") #append mode ..same file mein append ..'w' will del all the content and write the matter
# a = f.write("\nTarun has moved abroad")
# # content=f.read()
# # print(content)
# print(a) #returns numnber of characters in file
# f.close()

f=open("tarun2.txt","r+") #opens in r,w mode both
content=f.read()
a = f.write("\nTarun has moved abroad")
print(a) #returns numnber of characters in file
print(content)
f.close()
