# Author: Bojan G. Kalicanin
# Date: 11-Dec-2016
# Modeling Ship in the Sideway Shooter Game

import pygame

class Ship(object):
    """Modeling space ship."""
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Set ship's initial position on the left side of the screen.
        self.rect.left = self.screen_rect.left
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)