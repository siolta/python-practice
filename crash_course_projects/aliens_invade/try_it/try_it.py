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
        self.bg_color = (50, 55, 140)
        self.GAME_FONT = pygame.freetype.SysFont('Mono', 18)
        self.DEBUG = False
        self._key_press_debug = pygame.Surface((0, 0))

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
            self.character.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.DEBUG:
                    self._debug_keys(event)
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _debug_keys(self, event):
        # print(event.key)
        self._key_press_debug, _ = self.GAME_FONT.render(
            str(event.key), (0, 0, 0))

    def _check_keydown_events(self, event):
        """respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.character.moving_right = True
        if event.key == pygame.K_LEFT:
            self.character.moving_left = True
        if event.key == pygame.K_UP:
            self.character.moving_up = True
        if event.key == pygame.K_DOWN:
            self.character.moving_down = True

    def _check_keyup_events(self, event):
        """respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.character.moving_right = False
        if event.key == pygame.K_LEFT:
            self.character.moving_left = False
        if event.key == pygame.K_UP:
            self.character.moving_up = False
        if event.key == pygame.K_DOWN:
            self.character.moving_down = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        # print key inputs if DEBUG
        if self.DEBUG:
            self.screen.blit(self._key_press_debug,
                             self.screen.get_rect().midleft)
        self.character.blitme()

        pygame.display.flip()


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
        self.image = pygame.image.load('images/invader.png')
        self.rect = self.image.get_rect()

        # start at center of screen
        self.rect.center = self.screen_rect.center

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
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.char_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.char_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.char_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.char_speed

        # update char rect object
        self.rect.x = self.x
        self.rect.y = self.y


if __name__ == '__main__':
    game = TryIt()
    game.run_game()
