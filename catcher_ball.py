# Author: Bojan G. Kalicanin
# Date: 15-Dec-2016
# Ball object

import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    """Represent ball object."""
    def __init__(self, ai_settings, screen):
        super(Ball, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load ball image and get its rect.
        self.image = pygame.image.load("images/ball.bmp")
        self.rect = self.image.get_rect()

        # Set ball rect at (0, 0) position at top left part of screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save exact ball position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Blit ball image in its rect on the screen."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update ball position."""
        self.y += self.ai_settings.ball_speed_factor
        self.rect.y = self.y
