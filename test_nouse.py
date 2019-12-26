a=['a','b','c','d']
lgt = len(a)
b =['c','d','a','e']
for i in range(lgt):
    if b[i] in a:
        print(b[i])
        print('ok')