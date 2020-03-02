import pygame
from functions import load_image, unblock_side
from Collider import Collider


class Player(pygame.sprite.Sprite):
    def __init__(self, object_group, collider_group, x, y, health, speed):
        super().__init__()
        object_group.add(self)
        self.width = 100
        self.height = 100

        self.image = pygame.transform.scale(load_image('Main character (0%).jpg'), (self.width, self.height))
        self.moving_rect = list(self.image.get_rect())
        self.moving_rect[0] = x
        self.moving_rect[1] = y
        self.rect = pygame.Rect(self.moving_rect)
        self.collider = Collider(collider_group, self, 0, 0, self.width, self.height, trigger=False)

        self.tick = None
        self.health = health
        self.speed = speed
        self.direction_sides = []
        self.blocked_sides = [False, False, False, False]

    def update(self):
        self.moving(self.speed * self.tick)

    def moving(self, delta):
        if 'top' in self.direction_sides and not self.blocked_sides[0]:
            self.moving_rect[1] -= delta
            self.collider.moving_rect[1] -= delta
            unblock_side(self, 'bottom')
        if 'bottom' in self.direction_sides and not self.blocked_sides[2]:
            self.moving_rect[1] += delta
            self.collider.moving_rect[1] += delta
            unblock_side(self, 'top')
        if 'left' in self.direction_sides and not self.blocked_sides[3]:
            self.moving_rect[0] -= delta
            self.collider.moving_rect[0] -= delta
            unblock_side(self, 'right')
        if 'right' in self.direction_sides and not self.blocked_sides[1]:
            self.moving_rect[0] += delta
            self.collider.moving_rect[0] += delta
            unblock_side(self, 'left')

        self.rect = pygame.Rect(self.moving_rect)
        self.collider.rect = pygame.Rect(self.collider.moving_rect)