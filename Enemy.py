import pygame
from functions import load_image


class Enemy(pygame.sprite.Sprite):
    def __init__(self, group, x, y, health, speed, damage):
        super().__init__()
        group.add(self)
        self.width = 100
        self.height = 100

        self.image = pygame.transform.scale(load_image('Enemy.png'), (self.width, self.height))
        self.moving_rect = list(self.image.get_rect())
        self.moving_rect[0] = x
        self.moving_rect[1] = y
        self.rect = pygame.Rect(self.moving_rect)

        self.health = health
        self.speed = speed
        self.damage = damage
        self.player_is_found = False
        self.alive = True

    def run_to_player(self, player_x, player_y):
        if not self.player_is_found:
            return
        if (self.moving_rect[0] != player_x) and (self.moving_rect[1] != player_y):
            if player_x > self.moving_rect[0]:
                self.moving_rect[0] += self.speed
            else:
                self.moving_rect[0] -= self.speed

            if player_y > self.moving_rect[1]:
                self.moving_rect[1] += self.speed
            else:
                self.moving_rect[1] -= self.speed

    def hit_player(self, player):
        if (abs(self.moving_rect[1] - player.moving_rect[1]) <= 5) and (
                abs(self.moving_rect[0] - player.moving_rect[0]) <= 5):
            player.health -= self.damage

    def hit_enemy(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False
