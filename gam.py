import pygame
import os

#Creating screen with size 900x500
screen = pygame.display.set_mode((900, 500), pygame.RESIZABLE)

#Setting title + icon
pygame.display.set_caption("Space Invaders??")
icon = pygame.image.load('assets/spaceship_red.png')
pygame.display.set_icon(icon)
pygame.display.update

def mainuwu():
    #Game loop so it doesnt instantly close close
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #searching for player quit
                running = False
            if event.type == pygame.FULLSCREEN: #searching for player fullscreen
                pygame.display.toggle_fullscreen

if __name__ == "__main__":
    mainuwu()