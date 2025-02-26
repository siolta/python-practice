import pygame
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOT_SPEED,
    PLAYER_SHOT_COOLDOWN,
)
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.75
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self):
        # print(self.shot_timer)
        if self.shot_timer > 0:
            return
        self.shot_timer = PLAYER_SHOT_COOLDOWN
        shot = Shot(self.triangle()[0], self.position.y)
        shot.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_SHOT_SPEED

    def update(self, dt):
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_DOWN]:
            self.move(dt)
        if keys[pygame.K_UP]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        # wrap position on x axis
        if self.position[0] >= 1280:
            self.position[0] = 0
        elif self.position[0] <= 0:
            self.position[0] = 1280
        # wrap position on y axis
        elif self.position[1] >= 720:
            self.position[1] = 0
        elif self.position[1] <= 0:
            self.position[1] = 720
