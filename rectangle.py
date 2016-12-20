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
        
        self.rect.right = self.screen_rect.right - self.rect.width
        self.rect.top = self.screen_rect.top + self.rect.height

        self.top = float(self.rect.top)

        self.color = self.ai_settings.rect_color
        self.direction = 1 # Down direction of movement

    def update():
        """Update position of the rectangle on the screen."""
        if self.rect.top == self.screen_rect.top:
            self.direction = 1
        elif self.rect.top == self.screen_rect.bottom - self.rect.height:
            self.direction = 0
        self.top += self.ai_settings.speed_factor * self.direction

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.color, self.rect)