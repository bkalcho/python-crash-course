# Author: Bojan G. Kalicanin
# Date: 15-Dec-2016
# 13-3. Raindrops: Find an image of a raindrop and create a grid of
# raindrops. Make the raindrops fall toward the bottom of the screen
# until they disappear.

import pygame
import sys
from raindrop import Raindrop
from raindrops_settings import Settings

def run_game():
    pygame.init() # Initialize game
    ai_settings = Settings()
    # Create screen object (surface)
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height))
    pygame.display.set_caption("Raindrops Game")
    raindrop = Raindrop(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(ai_settings.bg_color)
        raindrop.blitme()
        pygame.display.flip()

run_game()