# Author: Bojan G. Kalicanin
# Date: 20-Dec-2016
# Bullets for rectangle game

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Models firing bullets in the game."""

    def __init__(self, ai_settings, screen, ship):
        """Initializes bullet class."""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                ai_settings.bullet_height)
        self.ship = ship
        self.ship_rect = self.ship.rect
        
        # Set bullet initial location.
        self.rect.centery = self.ship_rect.centery
        self.rect.left = self.ship_rect.right

        # Save precise bullet position.
        self.left = float(self.rect.left)

        self.color = self.ai_settings.bullet_color

    def update(self):
        """Update bullet position."""
        pass

    def draw_bullet(self):
        """Draw bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)