import pygame
from functions import load_image
from Collider import Collider


class TerrainObject(pygame.sprite.Sprite):
    object_images = {'spruce': load_image('Spruce.png'), 'grass bush': load_image('Grass bush.png')}

    def __init__(self, object_group, collider_group, type, x, y, width, height, speed):
        super().__init__()
        object_group.add(self)
        self.width = width
        self.height = height
        self.type = type
        self.speed = speed

        self.image = pygame.transform.scale(TerrainObject.object_images[self.type], (self.width, self.height))
        self.moving_rect = list(self.image.get_rect())
        self.moving_rect[0] = x
        self.moving_rect[1] = y
        self.rect = pygame.Rect(self.moving_rect)

        self.collider = None
        self.setup_collider(collider_group)

    def setup_collider(self, collider_group):
        if self.type == 'spruce':
            stem_width = int(self.width / 3.45)
            stem_depth = int(self.width / 6)
            self.collider = Collider(collider_group, self, (self.width - stem_width) / 2, self.height - stem_depth,
                                     stem_width, stem_depth, trigger=False)
        elif self.type == 'grass bush':
            bush_base_width = int(self.width / 1.85)
            self.collider = Collider(collider_group, self, (self.width - bush_base_width) / 2, self.height,
                                     bush_base_width, 0, trigger=False)