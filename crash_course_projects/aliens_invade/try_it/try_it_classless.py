
import sys

import pygame


# Does most of what 'try_it.py' does, but without classes

# Settings
pygame.init()
clock = pygame.time.Clock()
screen_width = 1200
screen_height = 800
bg_color = (49, 55, 139)
image = pygame.image.load('images/invader.png')
char_rect = image.get_rect()


def run_game():
    """start game loop"""
    while True:
        _check_events()
        _update_screen()
        clock.tick(60)


def _check_events():
    """Respond to keypresses and mouse events."""
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def _update_screen():
    """Update images on the screen, and flip to the new screen."""
    screen.fill(bg_color)

    screen.blit(image, char_rect)

    pygame.display.flip()


if __name__ == '__main__':
    screen = pygame.display.set_mode((screen_width,
                                      screen_height))
    pygame.display.set_caption("Trying things out classless")

    char_rect.center = screen.get_rect().center

    run_game()
