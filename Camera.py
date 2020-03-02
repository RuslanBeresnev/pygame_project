import pygame
from constants import WIDTH, HEIGHT
from functions import block_side, unblock_side


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0
        self.indent = HEIGHT // 5

        self.direction_sides = []
        self.blocked_sides = [False, False, False, False]
        self.tick = None

    def apply(self, obj):
        if 'top' in self.direction_sides and not self.blocked_sides[0]:
            obj.moving_rect[1] += self.dy
            if obj.collider is not None:
                obj.collider.moving_rect[1] += self.dy
            unblock_side(self, 'bottom')
        elif 'bottom' in self.direction_sides and not self.blocked_sides[2]:
            obj.moving_rect[1] += self.dy
            if obj.collider is not None:
                obj.collider.moving_rect[1] += self.dy
            unblock_side(self, 'top')
        if 'left' in self.direction_sides and not self.blocked_sides[3]:
            obj.moving_rect[0] += self.dx
            if obj.collider is not None:
                obj.collider.moving_rect[0] += self.dx
            unblock_side(self, 'right')
        elif 'right' in self.direction_sides and not self.blocked_sides[1]:
            obj.moving_rect[0] += self.dx
            if obj.collider is not None:
                obj.collider.moving_rect[0] += self.dx
            unblock_side(self, 'left')

        obj.rect = pygame.Rect(obj.moving_rect)
        if obj.collider is not None:
            obj.collider.rect = pygame.Rect(obj.collider.moving_rect)

    def update(self, target):
        self.dx = 0
        self.dy = 0
        self.direction_sides = []
        camera_works = False

        if target.rect.y <= self.indent:
            if 'top' in target.direction_sides:
                block_side(target, 'top')
                self.dy = target.speed * self.tick
                self.direction_sides.append('bottom')
                camera_works = True
            if not target.direction_sides:
                camera_works = True
        elif target.rect.y >= HEIGHT - self.indent - target.rect.height:
            if 'bottom' in target.direction_sides:
                block_side(target, 'bottom')
                self.dy = -target.speed * self.tick
                self.direction_sides.append('top')
                camera_works = True
            if not target.direction_sides:
                camera_works = True
        if target.rect.x <= self.indent:
            if 'bottom' in target.direction_sides:
                block_side(target, 'left')
                self.dx = target.speed * self.tick
                self.direction_sides.append('right')
                camera_works = True
            if not target.direction_sides:
                camera_works = True
        elif target.rect.x >= WIDTH - self.indent - target.rect.width:
            if 'right' in target.direction_sides:
                block_side(target, 'right')
                self.dx = -target.speed * self.tick
                self.direction_sides.append('left')
                camera_works = True
            if not target.dirrection_sides:
                camera_works = True

        return camera_works