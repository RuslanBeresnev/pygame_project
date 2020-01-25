import pygame
from functions import load_image, unblock_moving


class Player(pygame.sprite.Sprite):
    def __init__(self, group, x, y, speed):
        super().__init__(group)
        self.width = 150
        self.height = 150

        self.image = pygame.transform.scale(load_image('Main character (0%).jpg'), (self.width, self.height))
        self.moving_rect = list(self.image.get_rect())
        self.moving_rect[0] = x
        self.moving_rect[1] = y
        self.rect = pygame.Rect(self.moving_rect)

        self.tick = None
        self.speed = speed
        self.blocked_sides = [False, False, False, False]

    def update(self):
        self.moving()

    def moving(self):
        if pygame.key.get_pressed()[pygame.K_w] and not self.blocked_sides[0]:
            self.moving_rect[1] -= self.speed * self.tick
        if pygame.key.get_pressed()[pygame.K_s] and not self.blocked_sides[2]:
            self.moving_rect[1] += self.speed * self.tick
        if pygame.key.get_pressed()[pygame.K_a] and not self.blocked_sides[3]:
            self.moving_rect[0] -= self.speed * self.tick
        if pygame.key.get_pressed()[pygame.K_d] and not self.blocked_sides[1]:
            self.moving_rect[0] += self.speed * self.tick

        self.rect = pygame.Rect(self.moving_rect)
        unblock_moving(self)