import tut1
#if you will run the below line the output will have all the contents of tut1 even if you called msg()
# It is because when import a whole file , all the contents get executed so the functs getting called in file are also executed
print(tut1.msg("taurnb1"))

#added the calling functins in main and then run this and it will only print the ones being called from here
#also main function will retur different _name_ when run , when tut1 is run it will display main and when tut2 is run it will display tut1