# Author: Bojan G. Kalicanin
# Date: 15-Dec-2016
# Game functions

import pygame
import sys

def catch_events(catcher):
    """Cactch keyboard presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, catcher)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, catcher)


def check_keydown_events(event, catcher):
    """Check for key press events."""
    if event.key == pygame.K_LEFT:
        catcher.moving_left = True
    elif event.key == pygame.K_RIGHT:
        catcher.moving_right = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, catcher):
    """Check for key release events."""
    if event.key == pygame.K_LEFT:
        catcher.moving_left = False
    elif event.key == pygame.K_RIGHT:
        catcher.moving_right = False


def update_screen(ai_settings, screen, catcher):
    """Update Game screen."""
    screen.fill(ai_settings.bg_color)
    catcher.blitme()
    pygame.display.flip()