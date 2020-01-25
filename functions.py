import pygame
import os


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


def get_full_file_name(name):
    return os.path.join('data', name)


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


def set_objects_ticks(tick, *objects):
    for obj in objects:
        obj.tick = tick