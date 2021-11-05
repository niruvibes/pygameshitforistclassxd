import pygame
from pygame import surface #import pygame
import sys
import time


pygame.init() #initialize pygame module

# Creating screen with size 800x600 as default with resizable ability
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE) #add ", pygame.NOFRAME" to remove frame 

# Setting the title and icon
pygame.display.set_caption("Snake")
programIcon = pygame.image.load('resources/apple.jpg')
icon = pygame.image.load("programIcon")
pygame.display.set_icon(icon)
pygame.display.update


# Game loop so it doesnt close
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.FULLSCREEN:
            pygame.display.toggle_fullscreen

    screen.fill(pygame.Color("LIGHTBLUE")) 
    pygame.display.update()