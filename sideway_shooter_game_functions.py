# Author: Bojan G. Kalicanin
# Date: 11-Dec-2016
# Game functions

import pygame
import sys

def check_keydown_events(event, ship):
    """Catch keydown presses."""
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_UP:
        ship.moving_up = True

def check_keyup_events(event, ship):
    """Catch key releases."""
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    if event.key == pygame.K_UP:
        ship.moving_up = False

def check_events(ship):
    """Check keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    """Draw images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()