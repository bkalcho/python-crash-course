# Author: Bojan G. Kalicanin
# Date: 11-Dec-2016
# Modeling Ship in the Sideway Shooter Game

import pygame

class Ship(object):
    """Modeling space ship."""
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Set ship's initial position on the left side of the screen.
        self.rect.left = self.screen_rect.left
        self.rect.bottom = self.screen_rect.bottom

        # Movement flags.
        self.moving_up = False
        self.moving_down = False

        # Store a decimal value for the ship's bottom.
        self.bottom = float(self.rect.bottom)

    def update(self):
        """Update ship's position."""
        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor
        
        # Update rect object from self.bottom.
        self.rect.bottom = self.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)