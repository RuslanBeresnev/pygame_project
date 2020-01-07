import pygame
from functions import load_image, unblock_moving
from constants import FPS


class Player(pygame.sprite.Sprite):
    def __init__(self, group, x, y, speed):
        super().__init__(group)
        self.image = pygame.transform.scale(load_image('Главный персонаж - 0%.jpg'), (100, 100))
        self.moving_rect = list(self.image.get_rect())
        self.moving_rect[0] = x
        self.moving_rect[1] = y
        self.rect = pygame.Rect(self.moving_rect)

        self.speed = speed
        self.blocked_sides = [False, False, False, False]

    def update(self):
        if pygame.key.get_pressed()[pygame.K_w] and not self.blocked_sides[0]:
            self.moving_rect[1] -= self.speed / FPS
        if pygame.key.get_pressed()[pygame.K_s] and not self.blocked_sides[2]:
            self.moving_rect[1] += self.speed / FPS
        if pygame.key.get_pressed()[pygame.K_a] and not self.blocked_sides[3]:
            self.moving_rect[0] -= self.speed / FPS
        if pygame.key.get_pressed()[pygame.K_d] and not self.blocked_sides[1]:
            self.moving_rect[0] += self.speed / FPS

        self.rect = pygame.Rect(self.moving_rect)
        unblock_moving(self)