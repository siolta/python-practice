import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    """A class to represent a single enemy in the fleet."""

    def __init__(self, sideways_game, sprite_image):
        """Initialize the enemy and set its starting position."""
        super().__init__()
        self.screen = sideways_game.screen
        self.settings = sideways_game.settings

        # load the enemy image and set its rect attribute
        self.image = pygame.image.load(sprite_image)
        self.rect = self.image.get_rect()

        # start each enemy near the top righthand corner of the screen
        self.rect.x = self.settings.screen_width - self.rect.width
        self.rect.y = self.rect.height

    def check_edges(self):
        """Return True if enemy is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)

    def update(self):
        """move the enemy downward."""
        self.y += self.settings.enemy_speed * self.settings.enemy_direction
        self.rect.y = self.y
