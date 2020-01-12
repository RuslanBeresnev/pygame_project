import pygame
from functions import load_image


class Button(pygame.sprite.Sprite):
    def __init__(self, group, image, x, y, width, height):
        super().__init__(group)
        self.image = pygame.transform.scale(load_image(image), (int(width), int(height)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.w = width
        self.rect.h = height