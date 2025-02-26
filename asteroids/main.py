# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        update_screen(screen)

        # limit framerate to 60fps
        dt = clock.tick(60) / 1000


def update_screen(screen):
    screen.fill("black")
    pygame.display.flip()


if __name__ == "__main__":
    main()
