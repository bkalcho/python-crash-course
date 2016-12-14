# Author: Bojan G. Kalicanin
# Date: 14-Dec-2016
# Stars Game functions

import pygame
import sys
from star import Star

def check_events():
    """Catch keyboard presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

def update_screen(ai_settings, screen, stars):
    """Update screen surface."""
    screen.fill(ai_settings.bg_color)
    for star in stars.sprites():
        new_star = Star(ai_settings, screen)
    stars.draw(screen)
    pygame.display.flip()

def create_star(ai_settings, screen, stars, star_number, row_number):
    """Create star and place it in its location in the row."""
    star = Star(ai_settings, screen)
    star_width = star.rect.width
    star_height = star.rect.height
    star.x = star_width + 2 * star_width * star_number
    star.y = star_height + 2 * star_height * row_number
    star.rect.x = star.x
    star.rect.y = star.y
    stars.add(star)

def create_fleet(ai_settings, screen, stars):
    """Create row of stars."""
    star = Star(ai_settings, screen)
    star_width = star.rect.width
    star_height = star.rect.height
    available_space_x = ai_settings.screen_width - 2 * star_width
    number_stars_x = available_space_x // (2 * star_width)
    available_space_y = ai_settings.screen_height - 2 * star_height
    number_rows_y = available_space_y // (2 * star_height)
    for row_number in range(number_rows_y):
        for star_number in range(number_stars_x):
            create_star(ai_settings, screen, stars, star_number, row_number)