import pygame
from functions import load_image


class Cell(pygame.sprite.Sprite):
    cell_images = {'field': load_image('Field cell.jpg'), 'grass': load_image('Grass cell.jpg'),
                   'pebbles': load_image('Pebbles cell.jpg'), 'paving stones': load_image('Paving stones cell.jpg'),
                   'paving stones with grass': load_image('Paving stones with grass cell.jpg')}

    def __init__(self, group, type, x, y):
        super().__init__(group)
        self.width = 250
        self.height = 250

        self.image = pygame.transform.scale(Cell.cell_images[type], (self.width, self.height))
        self.moving_rect = list(self.image.get_rect())
        self.moving_rect[0] = x
        self.moving_rect[1] = y
        self.rect = pygame.Rect(self.moving_rect)