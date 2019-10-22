itm = ["1","2","3"]
mp=list(map(int,itm))
print(type(mp))


def sq(a):
    return a*a
itm = ["1","2","3"]
itm1=list(map(int,itm))
square =list(map(sq,itm1))
print(square)