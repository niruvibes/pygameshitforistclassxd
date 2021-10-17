import pygame
import os
import time

#Creating screen with size 900x500
screen = pygame.display.set_mode((900, 500), pygame.RESIZABLE)

#Setting title + icon
pygame.display.set_caption("Space Invaders??")
icon = pygame.image.load('assets/spaceship_red.png')
pygame.display.set_icon(icon)
pygame.display.update

#Setting FPS of game
FPS = 144

#Importing images
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))

def windraw(R, G, B):
    Color = R, G, B
    screen.fill(Color)
    pygame.display.update()

def mainuwu():
    clock = pygame.time.Clock() #setting clock variable
    #Game loop so it doesnt instantly close close
    running = True
    clock.tick(FPS)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #searching for player quit
                running = False
            if event.type == pygame.FULLSCREEN: #searching for player fullscreen
                pygame.display.toggle_fullscreen
            windraw(255, 255, 255)

#Failsafe incase this file is called upon thru an import
if __name__ == "__main__":
    mainuwu()