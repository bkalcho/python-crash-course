# Author: Bojan G. Kalicanin
# Date: 11-Dec-2016
# Sideway shooter game

import pygame
from sideway_shooter_settings import Settings
import sideway_shooter_game_functions as gf
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
    ship = Ship(ai_settings, screen)

    # Game main loop.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()