# Author: Bojan G. Kalicanin
# Date: 15-Dec-2016
# Game functions

import pygame
import sys
from catcher import Catcher
from catcher_ball import Ball
from random import randint
from time import sleep

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


def update_screen(ai_settings, screen, catcher, ball):
    """Update Game screen."""
    screen.fill(ai_settings.bg_color)
    catcher.draw(screen)
    ball.draw(screen)
    pygame.display.flip()


def update_ball(ai_settings, stats, screen, catcher, ball):
    """Update ball position and get rid of old ball."""
    screen_rect = screen.get_rect()
    ball.update()
    check_ball_bottom(stats, screen_rect, ball)
    if len(ball) == 0 and stats.balls_left > 0:
        new_b = Ball(ai_settings, screen)
        new_b.x = randint(new_b.rect.width, screen_rect.right - new_b.rect.width)
        new_b.rect.x = new_b.x
        new_b.y = new_b.rect.height
        new_b.rect.y = new_b.y
        ball.add(new_b)
    elif stats.balls_left == 0:
        stats.game_active = False
    # Detecting collisions
    collisions = pygame.sprite.groupcollide(ball, catcher, True, False)


def update_catcher(ai_settings, screen, catcher):
    screen_rect = screen.get_rect()
    catcher.update(ai_settings, screen)
    if len(catcher) == 0:
        c = Catcher(screen)
        c.center = screen_rect.centerx
        c.rect.centerx = c.center
        c.rect.bottom = screen_rect.bottom
        catcher.add(c)

def check_ball_bottom(stats, screen_rect, ball):
    """Check if ball reaches bottom of the screen."""
    for b in ball.copy():
        if b.rect.top >= screen_rect.bottom:
            ball.remove(b)
            stats.balls_left -= 1
            sleep(1.5)
            

