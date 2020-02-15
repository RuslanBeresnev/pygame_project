import pygame
from functions import load_image


class TerrainObject(pygame.sprite.Sprite):
    object_images = {'spruce': load_image('Spruce.png'), 'grass bush': load_image('Grass bush.png')}

    def __init__(self, group, type, x, y, width, height):
        super().__init__()
        group.add(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type

        self.image = pygame.transform.scale(TerrainObject.object_images[self.type], (self.width, self.height))
        self.moving_rect = list(self.image.get_rect())
        self.moving_rect[0] = x
        self.moving_rect[1] = y
        self.rect = pygame.Rect(self.moving_rect)