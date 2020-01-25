import pygame
import sys
import os
from constants import FPS, WIDTH, HEIGHT, TILE_HEIGHT, TILE_WIDTH
from functions import load_image, load_level
from Player import Player

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

tile_images = {'wall': load_image('box.png'), 'empty': load_image('grass.png')}

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            # потом добавим сюда остальные плитки, и игрока
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                # new_player = Player(player_group, x, y, 0)
    return new_player, x, y


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(TILE_WIDTH * pos_x, TILE_HEIGHT * pos_y)




# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             terminate()
#         elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
#             player, level_x, level_y = generate_level(load_level('map.txt'))  # начинаем игру
#             all_sprites.draw(screen)
#             tiles_group.draw(screen)
#             # player_group.draw(screen)
#             pygame.display.flip()
#     pygame.display.flip()
#     clock.tick(FPS)
#
# player, level_x, level_y = generate_level(load_level('map.txt'))
