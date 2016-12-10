# Author: Bojan G. Kalicanin
# Date: 10-Dec-2016
# Rocket Game settings file

class Settings(object):
    """Modeling Rocket Game settings."""
    def __init__(self):
        self.screen_width = 800
        self.scree_height = 600
        self.bg_color = (255, 255, 255)

        # Rocket settings.
        self.rocket_speed_factor = 2.2