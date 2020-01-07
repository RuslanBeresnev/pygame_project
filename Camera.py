import pygame
from constants import WIDTH, HEIGHT, FPS
from functions import block_moving


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0
        self.indent = 200

    def apply(self, obj):
        obj.rect.x += self.dx / FPS
        obj.rect.y += self.dy / FPS
        self.dx = 0
        self.dy = 0

    def update(self, target):
        if target.rect.y <= self.indent and pygame.key.get_pressed()[pygame.K_w]:
            block_moving(target, 'top')
            self.dy = target.speed
        if target.rect.x >= WIDTH - self.indent - target.rect.w and pygame.key.get_pressed()[pygame.K_d]:
            block_moving(target, 'right')
            self.dx = -target.speed
        if target.rect.y >= HEIGHT - self.indent - target.rect.h and pygame.key.get_pressed()[pygame.K_s]:
            block_moving(target, 'bottom')
            self.dy = -target.speed
        if target.rect.x <= self.indent and pygame.key.get_pressed()[pygame.K_a]:
            block_moving(target, 'left')
            self.dx = target.speed