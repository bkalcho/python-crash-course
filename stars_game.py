# Author: Bojan G. Kalicanin
# Date: 14-Dec-2016
# 13-1. Stars: Find an image of a star. Make a grid of stars appear on
# the screen.

import pygame
from stars_settings import Settings
import stars_game_functions as gf
from pygame.sprite import Group
#from star import Star

def run_game():
    """Main game function."""
    pygame.init()
    ai_settings = Settings()
    # Make screen surface.
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height))
    pygame.display.set_caption("Stars")

    # Make star object.
    #star = Star(ai_settings, screen)
    stars = Group()

    # Create fleet of stars.
    gf.create_fleet(ai_settings, screen, stars)

    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, stars)

run_game()