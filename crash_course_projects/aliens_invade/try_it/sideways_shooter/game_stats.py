import pygame


class GameStats:
    """Track statistics for sideways shooter."""

    def __init__(self, sideways_game):
        """Init stats."""
        self.settings = sideways_game.settings
        self.reset_stats()
        self._stats_surface = pygame.Surface((0, 0))

    def reset_stats(self):
        """initialize statistics that can change during the game."""
        self.character_lives = self.settings.char_lives
