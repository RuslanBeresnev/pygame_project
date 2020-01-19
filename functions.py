import pygame
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    return image


def block_moving(object, side):
    if side == 'top':
        object.blocked_sides[0] = True
    elif side == 'right':
        object.blocked_sides[1] = True
    elif side == 'bottom':
        object.blocked_sides[2] = True
    elif side == 'left':
        object.blocked_sides[3] = True


def unblock_moving(object):
    object.blocked_sides = [False, False, False, False]


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))
