import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """manages the bullet sprites fired by the character"""

    def __init__(self, sideways_game):
        """create a bullet object at the characters current position"""
        super().__init__()
        self.screen = sideways_game.screen
        self.settings = sideways_game.settings
        # settings
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 10
        self.bullet_color = (204, 204, 0)
        self.bullets_allowed = 3

        # create at (0, 0) and set position
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midright = sideways_game.character.rect.midright

        # store position as float
        self.x = float(self.rect.x)

    def update(self):
        """move the bullet across the screen"""
        # overwrites the builtin update in the sprite class
        self.x += self.bullet_speed
        # update the position
        self.rect.x = self.x

    def draw_bullet(self):
        """draw bullet to screen"""
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)
