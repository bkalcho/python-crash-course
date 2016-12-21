# Author: Bojan G. Kalicanin
# Date: 19-Dec-2016
# Game functions.

import pygame
import sys
from rectangle_bullet import Bullet
from rectangle import Rectangle
from time import sleep

def check_events(ai_settings, screen, ship, bullets):
    """Check for keyboard presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ai_settings, event, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(ai_settings, event, screen, ship, bullets):
    """Check for key presses."""
    if event.key == pygame.K_UP:
        ship.movement_up = True
    elif event.key == pygame.K_DOWN:
        ship.movement_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)


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


def fire_bullets(ai_settings, screen, ship, bullets):
    """Firing bullets in the game."""
    if len(bullets) < ai_settings.bullet_limit:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_bullet_rectangle_collisions(ai_settings, screen, rectangle, bullets):
    """Respond to bullet-rectangle collisions."""
    if pygame.sprite.spritecollideany(rectangle, bullets):
        bullets.empty()
        rectangle.reset_position()

        sleep(1.5)


def update_bullets(ai_settings, stats, screen, rectangle, bullets):
    screen_rect = screen.get_rect()
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.left >= screen_rect.right:
            bullets.remove(bullet)
            ai_settings.target_misses -= 1
        if ai_settings.target_misses == 0:
            stats.game_active = False

    check_bullet_rectangle_collisions(ai_settings, screen, rectangle, bullets)


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
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()