import pygame
import sys
import time
from subprocess import call
import random
from glob import glob
pygame.init()

audio_files = glob("audio/*.wav")

speed = [7,11] #14,7
size = width, height = 1280, 780
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lily roomba")
clock = pygame.time.Clock()
logo = pygame.image.load('roomba.png')
rect = logo.get_rect()
audio = random.choice(audio_files)
audio_copy = audio

def rot_center(image, angle):
    loc = image.get_rect().center  #rot_image is not defined 
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if (rect.left < 0 and (rect.top <= 7 or rect.bottom > 765)) or (rect.right > width and (rect.bottom > 765 or rect.top <= 15)) or (rect.top < 0 and (rect.left < 0 or rect.right > 1275)) or (rect.bottom > height and (rect.left < 0 or rect.right > 1275)):
        speed[0] = -speed[0]
        speed[1] = -speed[1]
        logo = rot_center(logo, 180)
        call(["afplay",'audio/dreamy-night.mp3'])

    elif rect.left < 0: 
        speed[0] = -speed[0]
        if speed[1] < 0: logo = rot_center(logo, 270)
        if speed[1] > 0: logo = rot_center(logo, 90)
        call(["afplay",audio])
        audio_copy = audio
        while audio_copy == audio: audio = random.choice(audio_files)
        
    elif rect.right > width: 
        speed[0] = -speed[0]
        if speed[1] < 0: logo = rot_center(logo, 90)
        if speed[1] > 0: logo = rot_center(logo, 270)
        call(["afplay",audio])
        audio_copy = audio
        while audio_copy == audio: audio = random.choice(audio_files)

    elif rect.top < 0: 
        speed[1] = -speed[1]
        if speed[0] < 0: logo = rot_center(logo, 90)
        if speed[0] > 0: logo = rot_center(logo, 270)
        call(["afplay",audio])
        audio_copy = audio
        while audio_copy == audio: audio = random.choice(audio_files)

    elif rect.bottom > height: 
        speed[1] = -speed[1]
        if speed[0] < 0: logo = rot_center(logo, 270)
        if speed[0] > 0: logo = rot_center(logo, 90)
        call(["afplay",audio])
        audio_copy = audio
        while audio_copy == audio: audio = random.choice(audio_files)

    rect.left += speed[0]
    rect.top  += speed[1]

    screen.fill((0,0,0))
    screen.blit(logo, rect)

    pygame.display.update()
    clock.tick(60)
