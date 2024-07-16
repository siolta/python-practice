import pygame


class Settings:
    """Container class for settings"""

    def __init__(self):
        """Initialize settings."""
        # Debug settings
        self.DEBUG = False

        # Font settings
        self.GAME_FONT = pygame.freetype.SysFont('Mono', 18)

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (192, 192, 192)

        # Character settings
        self.char_speed = 1.5
        self.char_lives = 0

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 1000
        self.bullet_color = (102, 0, 0)
        self.bullets_allowed = 3
        # setting behaviour is inverted
        self.piercing_rounds = False

        # Enemy settings
        self.enemy_speed = 1.0
        self.enemy_shift_speed = 200
        # fleet_dir of 1 is down; -1 is up
        self.enemy_direction = 1
