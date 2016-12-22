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
from rectangle_stats import GameStats
from rectangle_button import Button

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
    stats = GameStats(ai_settings)
    play_button = Button(screen, "Play")

    while True:
        # Main game loop.
        gf.check_events(ai_settings, stats, screen, rect, play_button, ship,
                            bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, stats, screen, rect, bullets)
            gf.rectangle_update(screen, rect)

        gf.update_screen(ai_settings, stats, screen, rect, ship, bullets,
                            play_button)


run_game()