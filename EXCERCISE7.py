#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#
# Rules
# Pygame module to play audio
#  pygame.mixer.music.load()
# Load a music file for playback
# load(filename) -> None
# load(object) -> None 
# import pygame
# import time
# file = 'music.mp3'
# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load(file)
# print(file)
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)

# if __name__ == "__main__":
# initial=time.time()
# localtime=time.asctime(time.localtime(initial))
# print(initial)
# time.sleep(5)
# final = time.time()
# if (final-initial >= 5):
    
#     run2()
#     if (input('Drank')):
#         pygame.mixer.music.stop()
# localtime1=time.asctime(time.localtime(final))
# print(final)

# def run2(self):
import time
import datetime
import pygame

def getdate():
    return datetime.datetime.now()

def reminder(mp3, stop_word, file):
    pygame.init()
   #

    while (True):
        if (input("Enter done if over: ")== stop_word):
            pygame.mixer.music.stop()
            with open(file,'a') as f:
                f.write("\n"+ str(getdate())+ " : "+ stop_word)
                print("Data Recorded successfully")
            break
        else:
            clock = pygame.time.Clock()
            clock.tick(10)
            while pygame.mixer.music.get_busy():
                pygame.event.poll()
                clock.tick(10)

def Time_limit(currenttime):
    if currenttime > '18:00:00' and currenttime < '23:00:01':
        return True
    else:
        print("Out of office time")
        return False

print("\t\t\t\t\t Welcome to Healthy Programmer System ")
print("\t\t\t\tI will keep your eyes and your body healthy")

water_level = 18

water_reminder = 10 #20 min
eyes_reminder = 30 #30 min
physical_reminder = 45 #45 min

currenttime = time.strftime('%H:%M:%S')
previous_water_time = time.time()
previous_eyeexercise_time = time.time()
previous_physicalexercise_time = time.time()

while(Time_limit(currenttime)):
    if water_level > 0:
        if (time.time() - previous_water_time) > water_reminder:  # water after every 20 minutes
            print("Time to drink water")
            while True :
                reminder('water.mp3', 'drank', 'water.txt')
                previous_water_time = time.time()
                water_level -= 1
                break
        if time.time() - previous_eyeexercise_time > eyes_reminder :
             print("Time to do eye exercise")
             while True :
                 reminder('eyes.mp3', 'eydone', 'eyes.txt')
                 previous_eyeexercise_time = time.time()
                 break
        if time.time() - previous_physicalexercise_time > physical_reminder :
             print("Time to do Physical exercise")
             while True :
                 reminder('excercise.mp3', 'exdone', 'physical.txt')
                 previous_physicalexercise_time = time.time()
                 break

print("\t\t\t\t\t\Bye! and Take care of your health")