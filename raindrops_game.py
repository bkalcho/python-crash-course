# Author: Bojan G. Kalicanin
# Date: 15-Dec-2016
# 13-3. Raindrops: Find an image of a raindrop and create a grid of
# raindrops. Make the raindrops fall toward the bottom of the screen
# until they disappear.

import pygame
import sys

def run_game():
    pygame.init() # Initialize game
    # Create screen object (surface)
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Raindrops Game")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.flip()

run_game()