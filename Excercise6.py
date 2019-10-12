# --10 times (while)
# ---max win is winner
# choose random SWG
#RULES --SNAKE-->WATER (w) water -->gun  gun-->snake
import random
attempts=0
cmp_wins=0
usr_wins=0
while(attempts<10):

    print("Enter your choice : \n 1.Snake --Press S \n2.Water --Press W \n 3.Gun --Press G")
    usr_inp = input()

    if    (usr_inp=='S'): print("Your selection : Snake")
    elif (usr_inp == 'W'): print("Your selection : Water")
    elif (usr_inp == 'G'): print("Your selection : Gun")
    else:
        print("Wrong input")
        break
    cmp_choices=["S","W","G"]
    cmp_inp=random.choice(cmp_choices)

    if    (cmp_inp=='S'): print("Computer selection : Snake")
    elif (cmp_inp == 'W'): print("Computer selection : Water")
    elif (cmp_inp == 'G'): print("Computer selection : Gun")

    if (cmp_inp =='S' and usr_inp == 'W'):
        cmp_wins=cmp_wins+1
        print("Computer wins ! \n Computer total wins:",cmp_wins)
    elif (cmp_inp == 'W'and usr_inp=='G'):
        cmp_wins = cmp_wins+1
        print("Computer wins ! \n Computer total wins:", cmp_wins)
    elif (cmp_inp == 'G' and usr_inp == 'S'):
        cmp_wins = cmp_wins+1
        print("Computer wins ! \n Computer total wins:", cmp_wins)
    elif (cmp_inp=='S'and usr_inp=='S'):
        print("Same selection ,NO RESULT ! try again!")
        continue
    elif (cmp_inp == 'W' and usr_inp == 'W'):
        print("Same selection !")
        continue
    elif (cmp_inp == 'G' and usr_inp == 'G'):
        print("Same selection !")
        continue
    else:
        usr_wins=usr_wins+1
        print("You win!! \n Your total wins :",usr_wins)
    attempts = attempts + 1
    print("Attempts left:",10-attempts)
print("Your total wins :",usr_wins)
print("Computer total wins :",cmp_wins)
if(cmp_wins>usr_wins):
    print("Winner is Computer")
else:
    print("You are the winner !")

