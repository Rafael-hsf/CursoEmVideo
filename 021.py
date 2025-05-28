#Faça um prgrama que abra e reproduza um arquivo MP3

import pygame
pygame.init()
pygame.mixer.music.load('m021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()