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

        # Bullet's settings.
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3