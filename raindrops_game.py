# Author: Bojan G. Kalicanin
# Date: 15-Dec-2016
# 13-3. Raindrops: Find an image of a raindrop and create a grid of
# raindrops. Make the raindrops fall toward the bottom of the screen
# until they disappear.

import pygame
import sys
from raindrop import Raindrop
from raindrops_settings import Settings
from pygame.sprite import Group
import raindrops_game_functions as gf

def run_game():
    pygame.init() # Initialize game
    ai_settings = Settings()
    # Create screen object (surface)
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height))
    pygame.display.set_caption("Raindrops Game")
    raindrops = Group()


    while True:
        gf.check_events()
        if ai_settings.new_grid:
            gf.create_grid(ai_settings, screen, raindrops)
        gf.raindrops_update(ai_settings, raindrops)
        gf.update_screen(ai_settings, screen, raindrops)

run_game()