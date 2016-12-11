# Author: Bojan G. Kalicanin
# Date: 11-Dec-2016
# Sideway Shooter Game Settings

class Settings(object):
    """Stores Sideway Shooter game settings."""
    def __init__(self):
        # Screen settings.
        self.width = 800
        self.height = 600
        self.bg_color = (255, 255, 255)

        # Ship's settings.
        self.ship_speed_factor = 1.5