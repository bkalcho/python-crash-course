# Author: Bojan G. Kalicanin
# Date: 19-Dec-2016
# Rectangle Game settings

class Settings(object):
    """Game settings."""
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        # Rectangle settings.
        self.rect_width = 35
        self.rect_height = 55
        self.rect_color = (0, 0, 0)
        self.speed_factor = 0.5

        # Ship settings.
        self.ship_speed_factor = 1.5

        # Bullet settings.
        self.bullet_width = 15
        self.bullet_height = 2
        self.bullet_color = (0, 0, 0)
        self.bullet_speed_factor = 3
        self.bullet_limit = 3