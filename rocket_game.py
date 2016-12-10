# Author: Bojan G. Kalicanin
# Date: 10-Dec-2016
# Main file of the Rocket game

import pygame
from rocket_settings import Settings
import game_functions as gf
from rocket import Rocket

def run_game():
    """Main function of the game."""
    
    # Initialize the game
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.scree_height))
    pygame.display.set_caption("Rocket Game")

    rocket = Rocket(ai_settings, screen)

    # Main loop of the game
    while True:
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(ai_settings, screen, rocket)

run_game()