
import time
initial=time.time()
print(initial)
for i in range(45):
    print("This is Tarun")
    time.sleep(2) #sleeps for 2 seconds
print("for loop time:",time.time()-initial)
initial2=time.time()
print(initial2)
k=0
while(k<45):
    print("This is Tarun")
    k=k+1
print("while loop time :",time.time()-initial2)
localtime=time.asctime(time.localtime(time.time()))
localtime1=time.localtime(time.time())
print(localtime)
print(localtime1) #this will return time in tuple format and we need in standard format therefore we use asctime funcn also
