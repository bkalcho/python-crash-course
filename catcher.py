# Author: Bojan G. Kalicanin
# Date: 15-Dec-2016
# Ball catcher character

import pygame
from pygame.sprite import Sprite

class Catcher(Sprite):
    """Models ball catcher in the game."""
    def __init__(self, screen):
        super(Catcher, self).__init__()
        self.screen = screen
        # Load character image and get its rectangle.
        self.image = pygame.image.load("images/catcher.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Set character rect in the bottom center position.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Save precise catcher position.
        self.center = float(self.rect.centerx)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False


    def update(self, ai_settings, screen):
        """Update catcher position."""
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.center += ai_settings.catcher_speed_factor
        if self.moving_left and self.rect.left >= 0:
            self.center -= ai_settings.catcher_speed_factor
        self.rect.centerx = self.center


    def blitme(self):
        """Blit character rectangle with image on the screen surface."""
        self.screen.blit(self.image, self.rect)