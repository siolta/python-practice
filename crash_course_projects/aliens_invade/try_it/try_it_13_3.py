import sys

import pygame
from pygame.sprite import Sprite
from random import randint

# TODO: Make it so when a row dissappears, a new row appears
# at the top of the screen and begins to fall


class TryIt:
    """Class to manage game assets and behaviours"""

    def __init__(self):
        """init game"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 50, 50)
        self.max_rain_sprites = 180

        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))
        pygame.display.set_caption("raindrops")
        self.raindrops = pygame.sprite.Group()

        self._create_raindrops()

        # set background color
        self.bg_color = (self.bg_color)

    def run_game(self):
        """start game loop"""
        while True:
            self._check_events()
            self._update_rain()
            print(len(self.raindrops))
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_rain(self):
        """Update raindrop positions."""
        self._check_rain_edge()
        self.raindrops.update()

    def _create_raindrops(self):
        """create a bunch of rain"""
        raindrop = Raindrop(self)
        drop_width, drop_height = raindrop.rect.size

        current_x, current_y = drop_width, drop_height
        while len(self.raindrops) < self.max_rain_sprites:
            while current_x < (self.screen_width - 2 * drop_width):
                self._create_drop(
                    randint(current_x, (current_x + 24)),
                    randint(current_y, (current_y + 26))
                )
                current_x += 2 * drop_width

            current_x = drop_width
            current_y += 2 * randint((drop_height // 2), drop_height)

    def _create_drop(self, x_pos, y_pos):
        """create a raindrop and place it in the row"""
        new_drop = Raindrop(self)
        new_drop.x = x_pos
        new_drop.y = y_pos
        new_drop.rect.x = x_pos
        new_drop.rect.y = y_pos
        self.raindrops.add(new_drop)

    def _check_rain_edge(self):
        """Respond to raindrops that have reached the bottom"""
        for rain_drop in self.raindrops.sprites():
            if rain_drop.check_edge():
                self.raindrops.remove(rain_drop)
                self._create_drop(
                    randint(rain_drop.x - 6, rain_drop.x + 6),
                    rain_drop.rect.height)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()


class Raindrop(Sprite):
    """class to manage raindrop sprites"""

    def __init__(self, try_it):
        """initialize character"""
        super().__init__()
        self.screen = try_it.screen

        # settings
        self.rain_speed = 3

        # load raindrop image and get rect
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        # start each new raindrop near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store raindrops's exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edge(self):
        """Return True if raindrop is at bottom edge of screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom)

    def update(self):
        self.y += self.rain_speed
        self.rect.y = self.y


if __name__ == '__main__':
    game = TryIt()
    game.run_game()
