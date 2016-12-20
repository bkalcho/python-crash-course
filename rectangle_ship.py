# Author: Bojan G. Kalicanin
# Date: 20-Dec-2016
# Ship class for rectangle game

import pygame

class Ship(object):
    """Models ship in game."""

    def __init__(self, ai_settings, screen):
        """Load image and get image rect."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.ai_settings = ai_settings

        # Set position of image rect.
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # Save ship's exact loacation.
        self.center = float(self.rect.centery)

        # Movement flags.
        self.movement_up = False
        self.movement_down = False

    def update(self):
        """Update ship position."""
        if self.movement_up and self.rect.top >= 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.movement_down and self.rect.bottom <= self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor
        self.rect.centery = self.center

    def blitme(self):
        """Show image rectangle on screen."""
        self.screen.blit(self.image, self.rect)