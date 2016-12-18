# Author: Bojan G. Kalicanin
# Date: 15-Dec-2016
# Catch Game settings

class Settings(object):
    """Game settings."""
    def __init__(self):
        # Game settings.
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        # Catcher settings.
        self.catcher_speed_factor = 1.5

        # Ball settings.
        self.ball_speed_factor = 0.10
        self.ball_limit = 3
