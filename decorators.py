# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...
# And so on, until the player gets the word.

import  re
word = 'EVAPORATE'
wordlength = len(word)
wordguess = '_'*wordlength
wordguess = list(wordguess)
# word = list(word)
guessesuser = []
while True:
    a = input('any alphabet guess \n')

    if a in guessesuser:
        print('already guessed')
        continue
    elif a in word:
        print('correct guess')
        for match in re.finditer(a, word):
            ind = match.start()
            wordguess[ind] = a
        print(wordguess)
    else:
        print('wrong guess , try again')
    if '_' not in wordguess:
            print('won')
            break
    guessesuser.append(a)

