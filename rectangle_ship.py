# Author: Bojan G. Kalicanin
# Date: 20-Dec-2016
# Ship class for rectangle game

import pygame

class Ship(object):
    """Models ship in game."""

    def __init__(self, screen):
        """Load image and get image rect."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Set position of image rect.
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Show image rectangle on screen."""
        self.screen.blit(self.image, self.rect)