#sum of 2 arrays
#line 1 ->> no of elements of array
#line2 ->>array 1 elemts
#line3 -->>array 2 elements
#line 4 -->output
arsum = []
size = int(input())
A =list(map(int,input().strip().split()))[:size]
B = list(map(int,input().strip().split()))[:size]
for i in range(size):
    arsum.append(A[i] + B[i])
for i in range(size):
    a = arsum[i]
    print(a,' ',end='')
# print(str(arsum))



#
# for i in range(size):
#     arsum.append(arr1[i] + ar2[i])
# print(arsum)
