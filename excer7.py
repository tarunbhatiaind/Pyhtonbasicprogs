from pygame import mixer
from time import time
from datetime import datetime

def musicplay(file,stopper):

    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True :
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log(text):
    with open('logs.txt','a') as f :
        f.write(f"{text}{datetime.now()}\n")


if __name__ == '__main__':

     log('drank water at :')
     waterinit = time()
     eyeinit = time()
     exinit = time()
     waterintvl = 5
     eyeintrvl = 10
     exintrvl = 15
     waterlevel = 3500
     while True:
        if time() - waterinit > waterintvl:
            if waterlevel>0:
                print('drink water')
                musicplay('water.mp3','drank')
                waterlevel-=200
                log('drank water at :')
                print(f'water left {waterlevel}')
            else:
                print('water over!')
                break
        if time() - eyeinit > eyeintrvl:
            print('eye interval')
            musicplay('eyes.mp3', 'eye')
            log('eye ex done at :')
        if time() - exinit > exintrvl:
            print('excercise')
            musicplay('excercise.mp3','ex')
            log('ex done at :')