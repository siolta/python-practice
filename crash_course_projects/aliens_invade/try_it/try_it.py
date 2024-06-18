import sys

import pygame


# TODO: Split the eva gif and animate the character

class TryIt:
    """Class to manage game assets and behaviours"""

    def __init__(self):
        """init game"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (49, 55, 139)

        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))
        pygame.display.set_caption("Trying things out")
        self.character = Character(self)

        # set background color
        self.bg_color = (self.bg_color)

    def run_game(self):
        """start game loop"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        self.character.blitme()

        pygame.display.flip()


class Character:
    """class to manage properties for initial game character"""

    def __init__(self, try_it_game):
        """initialize character"""
        self.screen = try_it_game.screen
        self.screen_rect = try_it_game.screen.get_rect()

        # load character image and get rect
        self.image = pygame.image.load('images/invader.png')
        self.rect = self.image.get_rect()

        # start at center of screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """draw character at current location."""
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    game = TryIt()
    game.run_game()
