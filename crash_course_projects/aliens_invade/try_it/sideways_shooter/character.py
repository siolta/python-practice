import pygame


class Character:
    """class to manage properties for initial game character"""

    def __init__(self, try_it_game):
        """initialize character"""
        self.screen = try_it_game.screen
        self.screen_rect = try_it_game.screen.get_rect()

        # movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # load character image and get rect
        self.image = pygame.image.load('images/defender.png')
        self.rect = self.image.get_rect()

        # start at center of screen
        self.rect.midleft = self.screen_rect.midleft

        # set speed value
        self.char_speed = 2.5

        # store float for characters's exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """draw character at current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the characters's position based on movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.char_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.char_speed

        # update char rect object
        self.rect.y = self.y

    def center_player(self):
        """center player char on screen edge."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
