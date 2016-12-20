# Author: Bojan G. Kalicanin
# Date: 19-Dec-2016
# Game functions.

import pygame
import sys

def check_events(ship):
    """Check for keyboard presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_kedown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_kedown_events(event, ship):
    """Check for key presses."""
    if event.key == pygame.K_UP:
        ship.movement_up = True
    elif event.key == pygame.K_DOWN:
        ship.movement_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullets()


def check_keyup_events(event, ship):
    """Check for key releasses."""
    if event.key == pygame.K_UP:
        ship.movement_up = False
    elif event.key == pygame.K_DOWN:
        ship.movement_down = False

def check_rectangle_direction(screen_rect, rect):
    if rect.rect.top <= screen_rect.top:
        rect.moving_down = True
        rect.moving_up = False
    elif rect.rect.bottom >= screen_rect.bottom:
        rect.moving_down = False
        rect.moving_up = True


def fire_bullets():
    """Firing bullets in the game."""
    pass


def rectangle_update(screen, rect):
    """Update position of the rectangle."""
    screen_rect = screen.get_rect()
    check_rectangle_direction(screen_rect, rect)
    rect.update()


def update_screen(ai_settings, screen, rect, ship, bullets):
    """Update game screen."""
    screen.fill(ai_settings.bg_color)
    rect.draw_rect()
    ship.blitme()
    bullets.draw(screen)
    pygame.display.flip()