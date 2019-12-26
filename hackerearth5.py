a = int(input())
i=1
while i<=a:
        
    i=i+1
    #  elements,steps= [int(elements) for elements in raw_input().split()] 
    inps = list(map(int,input().strip().split()))[:2]
    elements = inps[0]
    steps = inps[1]
    if steps > elements:
        steps = steps%elements
    #steps = int(input())
    arr = list(map(int,input().strip().split()))[:elements]
    length = len(arr)
    arr_temp=[None] *(length)
    print(len(arr_temp))
    
    for j in range(length):
        m =-length+j+steps
        # print(m,arr_temp[m])
        arr_temp[-length+j+steps] = arr[j]
     
        print(-length,j,steps,m,arr_temp[m])

    
    
    for k in arr_temp:
     print(k,end=' ')    
    print('\n')
    
