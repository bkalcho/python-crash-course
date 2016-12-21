# Author: Bojan G. Kalicanin
# Date: 19-Dec-2016
# Rectangle class

import pygame

class Rectangle(object):
    """Models rectangle in the game."""
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.rect = pygame.Rect(0, 0, self.ai_settings.rect_width,
            self.ai_settings.rect_height)
        
        self.rect.x = self.screen_rect.right - self.rect.width
        self.rect.y = self.screen_rect.top

        self.y = float(self.rect.y)

        self.color = self.ai_settings.rect_color
        
        # Movement flags
        self.moving_down = True
        self.moving_up = False

    def update(self):
        """Update position of the rectangle on the screen."""
        if self.moving_up and self.rect.top >= 0:
            self.y -= self.ai_settings.speed_factor
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.ai_settings.speed_factor
        self.rect.y = self.y

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def reset_position(self):
        """Put rectangle on start position."""
        self.y = self.screen_rect.top