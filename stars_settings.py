# Author: Bojan G. Kalicanin
# Date: 14-Dec-2016
# Settings class for Stars Game.

class Settings(object):
    """Class representing game settings."""
    def __init__(self):
        """Initialize game settings attributes."""
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)