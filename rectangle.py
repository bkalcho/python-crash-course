# Author: Bojan G. Kalicanin
# Date: 19-Dec-2016
# Rectangle class

import pygame

class Rectangle(object):
    """Models rectangle in the game."""
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0, 0, ai_settings.rect_width,
            ai_settings.rect_height)
        
        self.rect.x = self.screen_rect.right - self.rect.width
        self.rect.y = self.screen_rect.top + self.rect.height

        #self.y = float(self.rect.y)

        self.color = ai_settings.rect_color

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.color, self.rect)