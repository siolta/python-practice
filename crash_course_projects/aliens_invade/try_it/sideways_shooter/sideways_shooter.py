import sys
from time import sleep
from random import randint

import pygame

from settings import Settings
from game_stats import GameStats
from character import Character
from bullet import Bullet
from enemy import Enemy


class SidewaysShooter:
    """Class to manage game assets and behaviours"""

    def __init__(self):
        """init game"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.bg_color = self.settings.bg_color
        self.DEBUG = self.settings.DEBUG
        self._key_press_debug = pygame.Surface((0, 0))

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Slideways shootems")

        # create an instance of game stats
        self.stats = GameStats(self)

        self.character = Character(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self._create_fleet()

        # set background color
        self.bg_color = (self.bg_color)

        # Start game in 'active' state.
        self._game_active = True

    def run_game(self):
        """start game loop"""
        while True:
            self._check_events()

            if self._game_active:
                self.character.update()
                self._update_bullets()
                self._update_enemies()

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
        if event.key == pygame.K_UP:
            self.character.moving_up = True
        if event.key == pygame.K_DOWN:
            self.character.moving_down = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """respond to keypresses"""
        if event.key == pygame.K_UP:
            self.character.moving_up = False
        if event.key == pygame.K_DOWN:
            self.character.moving_down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # update bullet positions
        self.bullets.update()

        # remove bullets that have dissapeared
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
        if self.DEBUG:
            print(len(self.bullets))

        self._check_bullet_enemy_collisions()

    def _check_bullet_enemy_collisions(self):
        """respond to bullet enemy collisions."""
        # remove bullets and enemies that have collided
        # first bool is bullet removal
        if pygame.sprite.groupcollide(
                self.bullets, self.enemies,
                self.settings.piercing_rounds, True):
            self.stats.enemies_hit += 1

        if not self.enemies:
            # reset bullets and enemies
            self.bullets.empty()
            self._create_fleet()

    def _update_enemies(self):
        """Update position of all enemies in the fleet."""
        self._check_fleet_edges()
        self.enemies.update()

        # look for enemy-ship collisions
        if pygame.sprite.spritecollideany(self.character, self.enemies):
            self._character_hit()

        # look for enemies hitting the left side of the screen
        self._check_enemies_left()

    def _check_enemies_left(self):
        """check if any enemies have reached the left side of the screen"""
        for alien in self.enemies.sprites():
            if alien.rect.left <= 0:
                # treat the same as if the ship was hit
                self._character_hit()
                break

    def _create_fleet(self):
        """create the fleet of enemies"""
        # sprite1 is 29w x 28h
        # sprite2 is 25w x 26h
        # rough avg of 2 sprites to ensure they start on different collumns
        current_x = self.settings.screen_width - 25 * 3
        for enemy_type in ['images/enemy_sprite.png',
                           'images/enemy_sprite_2.png']:
            enemy = Enemy(self, enemy_type)
            enemy_width, enemy_height = enemy.rect.size

            current_y = enemy_height
            while current_y < (self.settings.screen_height - 3 * enemy_height):
                self._create_enemy(randint(
                    current_x, (current_x + enemy_height // 2)),
                    randint(
                    current_y, (current_y + enemy_width // 4)),
                    enemy_type)
                current_y += 2 * enemy_height

            # finished a collum; reset y val, increment x val
            current_y = enemy_height
            current_x -= 3 * enemy_width

    def _create_enemy(self, x_position, y_position, sprite_image):
        """create an enemy and place it."""
        new_enemy = Enemy(self, sprite_image)
        new_enemy.x = x_position
        new_enemy.y = y_position
        new_enemy.rect.x = x_position
        new_enemy.rect.y = y_position
        self.enemies.add(new_enemy)

    def _check_fleet_edges(self):
        """respond when enemies reach a screen edge."""
        for enemy in self.enemies.sprites():
            if enemy.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """shift fleet left, and change fleet direction."""
        for enemy in self.enemies.sprites():
            enemy.rect.x -= self.settings.enemy_shift_speed
        self.settings.enemy_direction *= -1

    def _character_hit(self):
        """respond to the player character being hit by an enemy."""
        if self.stats.character_lives > 0:
            self.stats.character_lives -= 1

            # Remove any leftover objects
            self.bullets.empty()
            self.enemies.empty()

            # create new fleet and reset player
            self._create_fleet()
            self.character.center_player()

            # Pause
            sleep(1)
        else:
            self._game_active = False

    def _end_game(self):
        """respond to game ending condition."""
        self._game_over_surface, _ = self.settings.GAME_FONT.render(
            "GAME OVER",
            (0, 0, 0))
        self.screen.blit(self._game_over_surface,
                         self.screen.get_rect().center)

    def _update_screen(self):
        """update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)

        # print key inputs if debug
        if self.DEBUG:
            self.screen.blit(self._key_press_debug,
                             self.screen.get_rect().midleft)

        self.stats.print_stats()

        self.character.blitme()
        self.enemies.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        if not self._game_active:
            self._end_game()

        pygame.display.flip()


if __name__ == '__main__':
    game = SidewaysShooter()
    game.run_game()
