# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from sys import exit
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = [asteroids, updatable, drawable]
    Shot.containers = [shots, updatable, drawable]
    AsteroidField.containers = [updatable]
    asteroid_field = AsteroidField()

    Player.containers = [updatable, drawable]
    player = Player(PLAYER_START_X, PLAYER_START_Y)

    # Time since last frame was drawn
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for sprite in asteroids:
            if sprite.is_colliding(player):
                print("Game over!")
                exit()

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        # limit framerate to 60fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
