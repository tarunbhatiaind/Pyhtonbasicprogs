# Monk's best friend Micro, who happen to be an awesome programmer, got him an integer matrix M of size  for his birthday. Monk is taking coding classes from Micro. They have just completed array inversions and Monk was successful in writing a program to count the number of inversions in an array. Now, Micro has asked Monk to find out the number of inversion in the matrix M. Number of inversions, in a matrix is defined as the number of unordered pairs of cells  such that .
# Monk is facing a little trouble with this task and since you did not got him any birthday gift, you need to help him with this task.
#
# Input:
# First line consists of a single integer T denoting the number of test cases.
# First line of each test case consists of one integer denoting N. Following N lines consists of N space separated integers denoting the matrix M.
#
# Output:
# Print the answer to each test case in a new line.
# sample input :
# 2
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# 2
# 4 3
# 1 4

# sample outout :
# 0
# 2
inps = int(input())
lst = []
for i in range(inps):
    Matrix =[]
    flag =0
    size = int(input())
    for k in range(size):
      Matrix.append(list(map(int,input().strip().split())))
    # print(Matrix)
    for j in range(size):
        for l in range(size):
            for x in range(size):
                for y in range(size):
                   if Matrix[j][l] > Matrix[x][y] and j<=x and l<=y:
                        flag=flag+1
    lst.append(flag)

length = len(lst)
for q in lst:
    print(q)





    # Matrix[0][2] = 5
    # print(Matrix)