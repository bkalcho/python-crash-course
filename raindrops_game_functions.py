# Author: Bojan G. Kalicanin
# Date: 15-Dec-2016
# Raindrops Game functions

import pygame
import sys
from raindrop import Raindrop

def check_events():
    """Check keyboard key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

def update_screen(ai_settings, screen, raindrops):
    """Update screen."""
    screen.fill(ai_settings.bg_color)
    for raindrop in raindrops.sprites():
        new_raindrop = Raindrop(screen)
    raindrops.draw(screen)
    pygame.display.flip()

def create_raindrop(ai_settings, screen, raindrops, raindrop_number):
    """Create raindrop object at its location."""
    raindrop = Raindrop(screen)
    raindrop_width = raindrop.rect.width
    raindrop_height = raindrop.rect.height
    raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
    raindrop.rect.x = raindrop.x
    raindrops.add(raindrop)

def create_grid(ai_settings, screen, raindrops):
    raindrop = Raindrop(screen)
    raindrop_width = raindrop.rect.width
    available_space_x = ai_settings.screen_width - 2 * raindrop_width
    number_raindrops_x = available_space_x // (2 * raindrop_width)
    for raindrop_number in range(number_raindrops_x):
        create_raindrop(ai_settings, screen, raindrops, raindrop_number)
    ai_settings.new_grid = False

def raindrops_update(ai_settings, raindrops):
    """Update position of all raindrops in the grid."""
    for raindrop in raindrops.sprites():
        raindrop.y += ai_settings.raindrop_speed_factor
        raindrop.rect.y = raindrop.y
        if raindrop.rect.y >= ai_settings.screen_height:
            for raindrop in raindrops.copy():
                raindrops.remove(raindrop)
            ai_settings.new_grid = True