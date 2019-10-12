print("Enter no. of rows :: ")
row = int(input())
i = 1

print("Enter 0 or 1 :: ")
ch = int(input())
bool(ch)


while row > 0:
    if ch:
        print(i * "*")

    else:
        print(row * "*")

    i = i + 1
    row = row - 1