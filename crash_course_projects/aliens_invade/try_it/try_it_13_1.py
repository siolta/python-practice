import sys

import pygame
from pygame.sprite import Sprite
from random import randint


class TryIt:
    """Class to manage game assets and behaviours"""

    def __init__(self):
        """init game"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))
        pygame.display.set_caption("Star field")
        self.stars = pygame.sprite.Group()

        self._create_starfield()

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

    def _create_starfield(self):
        """create a field of stars"""
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (self.screen_height - 3 * star_height):
            while current_x < (self.screen_width - 2 * star_width):
                self._create_star(
                    randint(current_x, (current_x + 24)),
                    randint(current_y, (current_y + 26))
                )
                current_x += 2 * star_width

            current_x = star_width
            current_y += 2 * star_height

    def _create_star(self, x_pos, y_pos):
        """create a star and place it in the row"""
        new_star = Star(self)
        new_star.x = x_pos
        new_star.y = y_pos
        new_star.rect.x = x_pos
        new_star.rect.y = y_pos
        self.stars.add(new_star)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


class Star(Sprite):
    """class to manage star sprites"""

    def __init__(self, try_it):
        """initialize character"""
        super().__init__()
        self.screen = try_it.screen

        # load star image and get rect
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # start each new star near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # stor star's exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


if __name__ == '__main__':
    game = TryIt()
    game.run_game()
