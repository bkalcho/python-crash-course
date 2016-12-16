# Author: Bojan G. Kalicanin
# Date: 15-Dec-2016
# Raindrops Game settings

class Settings(object):
    """Raindrops Game settings."""
    def __init__(self):
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        # Raindrop Settings
        self.raindrop_speed_factor = 0.75
        self.new_grid = True