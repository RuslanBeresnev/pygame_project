import pygame
from functions import load_image


class Background(pygame.sprite.Sprite):
    def __init__(self, group, image, x, y):
        super().__init__(group)
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y