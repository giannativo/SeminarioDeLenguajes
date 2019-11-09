'''
Created on 1 nov. 2016

@author: Javier Rodriguez
'''

#Pygame template 

import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

#Definir colores
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Iniciar pygame y creaer ventana
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()

all_sprites= pygame.sprite.Group()

#Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
                    
    # Update
    all_sprites.update()
    
    # Render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # After loading everything, flip the screen
    pygame.display.flip()

    