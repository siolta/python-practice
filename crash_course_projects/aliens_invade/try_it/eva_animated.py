import sys

import pygame

# TODO: transparancy the frames, and re enable movement


class EvaAnimated:
    """Class to manage game assets and behaviours"""

    def __init__(self):
        """init game"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 55, 140)

        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))
        pygame.display.set_caption("Test animation")
        self.eva = Eva(self)

        # set background color
        self.bg_color = (self.bg_color)

    def run_game(self):
        """start game loop"""
        while True:
            self._check_events()
            self.eva.update()
            self._update_screen()
            self.clock.tick(30)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        self.eva.blitme()

        pygame.display.flip()


class Eva:
    """class to manage properties for Eva animation"""

    def __init__(self, eva_animation):
        """initialize Eva"""
        self.screen = eva_animation.screen
        self.screen_rect = eva_animation.screen.get_rect()

        # load Eva image and get rect
        self.frames = [pygame.image.load(
            f'images/eva_animated_sprites/frame_{i:02}.gif') for i in range(18)]

        self.frame = 0

        self.image = self.frames[self.frame]

        self.rect = self.image.get_rect()

        # start at center of screen
        self.rect.center = self.screen_rect.center

        # store float for Eva's exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """draw Eva at current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.frame += 1

        if self.frame >= len(self.frames):
            self.frame = 0

        self.image = self.frames[self.frame]


if __name__ == '__main__':
    game = EvaAnimated()
    game.run_game()
