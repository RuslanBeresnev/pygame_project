import pygame
from functions import load_image


class Enemy(pygame.sprite.Sprite):
    def __init__(self, group, x, y, type, speed, damage, helth):
        super().__init__(group)
        self.image = pygame.transform.scale(load_image(type + '.jpg'), (self.width, self.height))
        self.moving_rect = list(self.image.get_rect())
        self.moving_rect[0] = x
        self.moving_rect[1] = y
        self.rect = pygame.Rect(self.moving_rect)
        self.player_is_found = False
        self.speed = speed
        self.damage = damage
        self.helth = helth
        self.alive = True

    def run_to_player(self, x, y):
        if not self.player_is_found:
            return
        if (self.moving_rect[0] != x) and (self.moving_rect[1] != y):
            # допилить движение с одной и той же скоростью
            if x > self.moving_rect[0]:
                self.moving_rect[0] += self.speed
            else:
                self.moving_rect[0] -= self.speed

            if y > self.moving_rect[1]:
                self.moving_rect[1] += self.speed
            else:
                self.moving_rect[1] -= self.speed

    def hit_player(self, player):
        if (abs(self.moving_rect[1] - player.moving_rect[1]) <= 5) and (
                abs(self.moving_rect[0] - player.moving_rect[0]) <= 5):
            player.hp -= self.damage
            print('player hited')

    def hit_enemy(self, damage):
        self.helth -= damage
        if self.helth <= 0:
            self.alive = False
