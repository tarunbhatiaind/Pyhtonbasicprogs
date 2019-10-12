def datalog(a) :
    """Function to lof data for users in file"""
    print("What data you would like to log for "+a)
    print("\n 1.Press 1 for Diet \n 2.Press 2 for excercise")
    choice=int(input())
    if(choice==1) :
        f=open(a+"_diet.txt","a")
        val=input('type the diet for user here \n')
        f.write(str(getdate())+ val+"\n")
        f.close()
    elif (choice ==2) :
        f = open(a+ "_excercise.txt", "a")
        val = input('type the excercise for user here \n')
        f.write(str(getdate()) + val + "\n")
        f.close()
    else:
        print("wrong choice !")

def getdate():
    """Function to retreive current time and date"""
    import datetime
    return datetime.datetime.now()

def datartr(b) :
    """Function to retreive data for users in file"""
    print("What data you want to see ? \n 1. Press 1 for Diet \n 2. Press 2 for excercise")
    rchoice= int(input())
    if (rchoice==1) :
        f=open(b+"_diet.txt","rt")
        content = f.read()
        print(content)
        f.close()
    elif (rchoice==2) :
        f = open(b + "_excercise.txt", "rt")
        content = f.read()
        print(content)
        f.close()
#Main Program :
i='y'
while (i is not 'n'):

    print("Please enter the user for which you want to log the data:\n 1.Press 1 for Harry \n 2.Press 2 for Hamaad \n 3.Press 3 for Rohan")
    usr=int(input())
    if (usr==1):
        datalog('Harry')
    elif (usr==2) :
        datalog('Hamaad')
    elif (usr==3) :
        datalog('Rohan')
    else :
        print("Wrong choice !")
    print("Your data has been logged !")
    print("Please enter the user for which you want to retreive the data:\n 1.Press 1 for Harry \n 2.Press 2 for Hamaad \n 3.Press 3 for Rohan")
    rtr=int(input())
    if (rtr==1):
        datartr('Harry')
    elif (rtr==2) :
        datartr('Hamaad')
    elif (rtr==3) :
        datartr('Rohan')
    else :
        print("Wrong choice !!")
    print("Do you wish to continue?y/n")
    i=input()
    continue