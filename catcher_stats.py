# Author: Bojan G. Kalicanin
# Date: 18-Dec-2016
# Catcher game statistics.

class GameStats(object):
    """Track game statistics."""

    def __init__(self, ai_settings):
        """Initialize game statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Game active flag.
        self.game_active = True

    def reset_stats(self):
        """
        Initialize game statistics which can change during game play.
        """
        self.balls_left = self.ai_settings.ball_limit