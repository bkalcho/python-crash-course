# Author: Bojan G. Kalicanin
# Date: 11-Dec-2016
# Sideway shooter game

import pygame
import sys

def run_game():
    """Main Sideway shooter game program."""

    # Initialize game.
    pygame.init()
    # Create screen surface
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Sideway Shooter")

    # Game main loop.
    while True:
        # Catch keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Draw screen.
        pygame.display.flip()

run_game()