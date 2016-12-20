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


def check_rectangle_direction(screen_rect, rect):
    if rect.rect.top <= screen_rect.top:
        rect.moving_down = True
        rect.moving_up = False
    elif rect.rect.bottom >= screen_rect.bottom:
        rect.moving_down = False
        rect.moving_up = True


def rectangle_update(screen, rect):
    """Update position of the rectangle."""
    screen_rect = screen.get_rect()
    check_rectangle_direction(screen_rect, rect)
    rect.update()
    #print("UP", rect.moving_up, "DOWN", rect.moving_down)


def update_screen(ai_settings, screen, rect):
    """Update game screen."""
    screen.fill(ai_settings.bg_color)
    rect.draw_rect()
    pygame.display.flip()