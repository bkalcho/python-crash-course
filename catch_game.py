# Author: Bojan G. Kalicanin
# Date: 15-Dec-2016
# 13-5. Catch: Create a game that places a character that you can move
# left and right at the bottom of the screen. Make a ball appear at a
# random position at the top of the screen and fall down the screen at a
# steady rate. If your character "catches" the ball by colliding with
# it, make the ball disappear. Make a new ball each time your character
# catches the ball or whenever the ball disappears off the bottom of the
# screen.

import pygame
import sys
from catch_settings import Settings
import catch_game_functions as gf
from catcher import Catcher
from catcher_ball import Ball

def run_game():
    """Main game program."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height))
    pygame.display.set_caption("Catch Game")
    # Catcher object.
    catcher = Catcher(screen)
    # Ball object.
    ball = Ball(screen)

    # Main game loop.
    while True:
        gf.catch_events(catcher)
        catcher.update(ai_settings, screen)
        gf.update_screen(ai_settings, screen, catcher, ball)


run_game()