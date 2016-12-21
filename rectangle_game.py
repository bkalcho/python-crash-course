# Author: Bojan G. Kalicanin
# Date: 19-Dec-2016
# 14-2. Target Practice: Create a rectangle at the right edge of the
# screen that moves up and down at a steady rate. Then have a ship
# appear on the left side of the screen that the player can move up and
# down while firing bullets at the moving, rectangular target. Add a
# Play button that starts the game, and when the player misses the
# target three times, end the game and make the Play button reappear.
# Let the player restart the game with this Play button.

import pygame
from rectangle_settings import Settings
import rectangle_game_functions as gf
from rectangle import Rectangle
from rectangle_ship import Ship
from pygame.sprite import Group

def run_game():
    """Main game program."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                    ai_settings.screen_height))
    pygame.display.set_caption("Rectangle Game")
    rect = Rectangle(ai_settings, screen)
    ship = Ship(ai_settings, screen)
    bullets = Group()

    while True:
        # Main game loop.

        gf.check_events(ai_settings, screen, ship, bullets)
        gf.rectangle_update(screen, rect)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, rect, ship, bullets)


run_game()