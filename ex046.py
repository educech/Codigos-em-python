from time import sleep
for c in range (10, 0,-1):
    print(c)
    sleep(1)
print("BOOM  BOOM POOW")
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex46.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
