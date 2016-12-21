# Author: Bojan G. Kalicanin
# Date: 21-Dec-2016
# Game statistics

class GameStats(object):
    """Track statistics for Rectangle Game."""

    def __init__(self, ai_settings):
        """Initializing statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True # Start game in inactive state.
    
    def reset_stats(self):
        """Initialize statistics."""
        self.target_misses = self.ai_settings.target_misses
