# Author: Bojan G. Kalicanin
# Date: 14-Dec-2016
# Star class definition.

import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Models star object."""
    def __init__(self, ai_settings, screen):
        super(Star, self).__init__()
        self.screen = screen
        # Load star image and get rect
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # Set star rect at top left position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save exact position of star
        self.x = float(self.rect.x)

    def blitme(self):
        """Blit star rectangle with star image on the screen."""
        self.screen.blit(self.image, self.rect)