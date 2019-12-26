import datetime
old_time = datetime.datetime.now()
print(old_time)
a=0
b=1
if(a<b):
    new_time = old_time - datetime.timedelta(hours=2, minutes=10)
    print(new_time)