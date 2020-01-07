import pygame
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()

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