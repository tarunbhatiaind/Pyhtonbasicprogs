flag = 0
while(flag<5):

    n=18
    print("Number of guesses left:",5-flag)
    flag = flag + 1
    var1 = int(input("Guess a number\n"))
  #  if(flag==5):
   #     print("You are out of guesses now , run the program again!")
    #    break
    if(var1==n):
        print("Correct Number!!!!!!\n ")
        print("Number of guesses you took:",flag)
        break
    elif(var1>n):
        print("try a lesser number!!\n")
        continue
    else:
        print("Try a larger number!!\n")
        continue
print("You are out of guesses!!GAME OVER !!")