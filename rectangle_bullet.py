# Author: Bojan G. Kalicanin
# Date: 20-Dec-2016
# Bullets for rectangle game

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Models firing bullets in the game."""

    def __init__(self, ai_settings, screen):
        """Initializes bullet class."""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                ai_settings.bullet_height)