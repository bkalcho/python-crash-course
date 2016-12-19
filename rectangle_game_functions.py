# Author: Bojan G. Kalicanin
# Date: 19-Dec-2016
# Game functions.

import pygame
import sys

def check_events():
    """Check for keyboard presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, rect):
    """Update game screen."""
    screen.fill(ai_settings.bg_color)
    rect.draw_rect()
    pygame.display.flip()