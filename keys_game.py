# Author: Bojan G. Kalicanin
# Date: 10-Dec-2016
# Key pressing game

import sys
import pygame

def run_game():
    # Main game program.
    
    # Initialize the game.
    pygame.init()
    # Make a screen surface
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Key presses game")
    while True:
        # Catches events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
    
        pygame.display.flip()

run_game()