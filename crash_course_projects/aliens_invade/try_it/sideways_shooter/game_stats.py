class GameStats:
    """Track statistics for sideways shooter."""

    def __init__(self, sideways_game):
        """Init stats."""
        self.settings = sideways_game.settings
        self.screen = sideways_game.screen
        self.reset_stats()

    def reset_stats(self):
        """initialize statistics that can change during the game."""
        self.character_lives = self.settings.char_lives
        self.enemies_hit = 0

    def print_stats(self):
        """print out the game stats to the screen"""
        char_lives = "Lives Left: {}"
        enemies_shot = "Enemies hit: {}"
        # prep lives image
        self._lives_surface, _ = self.settings.GAME_FONT.render(
            char_lives.format(self.character_lives),
            (30, 30, 30))
        self.screen.blit(self._lives_surface,
                         self.screen.get_rect().midtop)
        # prep kills image
        self._enemies_score, _ = self.settings.GAME_FONT.render(
            enemies_shot.format(self.enemies_hit),
            (0, 0, 0))
        # set the position of the kills image
        self._enemy_score_rect = self._enemies_score.get_rect()
        self._enemy_score_rect.right = self.screen.get_rect().right - 20
        self._enemy_score_rect.top = 20
        # draw enemy kills to screen
        self.screen.blit(self._enemies_score,
                         self._enemy_score_rect)
