# Author: Bojan G. Kalicanin
# Date: 10-Dec-2016
# Functions which control the flow of the game

import pygame
import sys

def check_keydown_events(event, rocket):
    """Check for key presses."""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True
    elif event.key == pygame.K_UP:
        rocket.moving_up = True

def check_keyup_events(event, rocket):
    """Check for key releases."""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False

def check_events(rocket):
    """Check for keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)

def update_screen(ai_settings, screen, rocket):
    """Update game screen."""
    screen.fill(ai_settings.bg_color)
    rocket.blitme()
    pygame.display.flip()