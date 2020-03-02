import pygame
from functions import load_image


class Cell(pygame.sprite.Sprite):
    width = 180
    height = 180
    cell_images = {'field': load_image('Field cell.jpg'),
                   'pebbles': load_image('Pebbles cell.jpg'), 'paving stones': load_image('Paving stones cell.jpg'),
                   'paving stones with grass': load_image('Paving stones with grass cell.jpg'),
                   'trail': load_image('Trail cell.jpg')}

    def __init__(self, group, type, x, y, speed):
        super().__init__()
        group.add(self)
        self.type = type
        self.speed = speed

        self.image = pygame.transform.scale(Cell.cell_images[self.type], (self.width, self.height))
        self.moving_rect = list(self.image.get_rect())
        self.moving_rect[0] = x
        self.moving_rect[1] = y
        self.rect = pygame.Rect(self.moving_rect)
        self.collider = None