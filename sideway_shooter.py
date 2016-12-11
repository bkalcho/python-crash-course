# Author: Bojan G. Kalicanin
# Date: 11-Dec-2016
# Sideway shooter game

import pygame
from sideway_shooter_settings import Settings
import sys
from sideway_shooter_ship import Ship

def run_game():
    """Main Sideway shooter game program."""

    # Initialize game.
    pygame.init()
    ai_settings = Settings()
    # Create screen surface
    screen = pygame.display.set_mode((ai_settings.width,
        ai_settings.height))
    pygame.display.set_caption("Sideway Shooter")
    ship = Ship(screen)

    # Game main loop.
    while True:
        # Catch keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(ai_settings.bg_color)
        # Draw ship on the screen
        ship.blitme()
        # Draw screen.
        pygame.display.flip()

run_game()