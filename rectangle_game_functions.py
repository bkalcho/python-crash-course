# Author: Bojan G. Kalicanin
# Date: 19-Dec-2016
# Game functions.

import pygame
import sys
from rectangle_bullet import Bullet
from rectangle import Rectangle
from time import sleep

def check_events(ai_settings, stats, screen, rect, play_button, ship, bullets):
    """Check for keyboard presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ai_settings, event, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, rect, ship, bullets, play_button, mouse_x,
                                mouse_y)


def check_play_button(stats, rect, ship, bullets, play_button, mouse_x,
                        mouse_y):
    """Start a new game when player presses button."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Hide mouse cursor.
        pygame.mouse.set_visible(False)

        start_game(stats, rect, ship, bullets)


def start_game(stats, rect, ship, bullets):
    """Start new game."""
    # Reset Game statistics.
    stats.reset_stats()
    stats.game_active = True

    # Destroy all bullets.
    bullets.empty()

    # Center the ship, and reset rectangle position.
    ship.center_ship()
    rect.reset_position()


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
            stats.target_misses_left -= 1
        if stats.target_misses_left == 0:
            stats.game_active = False
            pygame.mouse.set_visible(True)

    check_bullet_rectangle_collisions(ai_settings, screen, rectangle, bullets)


def rectangle_update(screen, rect):
    """Update position of the rectangle."""
    screen_rect = screen.get_rect()
    check_rectangle_direction(screen_rect, rect)
    rect.update()


def update_screen(ai_settings, stats, screen, rect, ship, bullets, play_button):
    """Update game screen."""
    screen.fill(ai_settings.bg_color)
    rect.draw_rect()
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()