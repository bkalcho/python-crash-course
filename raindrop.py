# Author: Bojan G. Kalicanin
# Date: 15-Dec-2016
# Raindrop class

import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """Class describing raindrop object."""
    def __init__(self, screen):
        """Initialize class."""
        super(Raindrop, self).__init__()
        self.screen = screen

        # Load raindrop image and get its rect
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Set raindrop position on the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save exact position of star
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Set raindrop on the screen."""
        self.screen.blit(self.image, self.rect)