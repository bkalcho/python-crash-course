# Author: Bojan G. Kalicanin
# Date: 19-Dec-2016
# Rectangle Game settings

class Settings(object):
    """Game settings."""
    def __init__(self):
        """Initialize static game settings."""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        # Rectangle settings.
        self.rect_width = 35
        self.rect_height = 55
        self.rect_color = (0, 0, 0)

        # Bullet settings.
        self.bullet_width = 15
        self.bullet_height = 2
        self.bullet_color = (0, 0, 0)
        self.bullet_limit = 3
        self.target_misses_limit = 3

        # Add leveling up tempo.
        self.speedup_scale = 1.1

        # Initialize game's settings that change throughout a game.
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize dynamic settings."""
        self.speed_factor = 0.1     # Rectangle speed

        # Ship settings.
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 3

    def speedup_game(self):
        self.speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
