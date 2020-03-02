import pygame
import os
from constants import SCREEN

previous_collide_verdicts = []


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


def get_full_file_name(name):
    return os.path.join('data', name)


def determine_direction(entity):
    entity.direction_sides = []

    if pygame.key.get_pressed()[pygame.K_w]:
        entity.direction_sides.append('top')
    if pygame.key.get_pressed()[pygame.K_s]:
        entity.direction_sides.append('bottom')
    if pygame.key.get_pressed()[pygame.K_a]:
        entity.direction_sides.append('left')
    if pygame.key.get_pressed()[pygame.K_d]:
        entity.direction_sides.append('right')


def block_side(object, side):
    if side == 'top':
        object.blocked_sides[0] = True
    elif side == 'right':
        object.blocked_sides[1] = True
    elif side == 'bottom':
        object.blocked_sides[2] = True
    elif side == 'left':
        object.blocked_sides[3] = True


def unblock_side(object, side):
    if side == 'top':
        object.blocked_sides[0] = False
    elif side == 'right':
        object.blocked_sides[1] = False
    elif side == 'bottom':
        object.blocked_sides[2] = False
    elif side == 'left':
        object.blocked_sides[3] = False


def set_objects_ticks(tick, *objects):
    for obj in objects:
        obj.tick = tick


def draw_group_contour(group, color, thickness):
    for sprite in group.get_sprites():
        pygame.draw.rect(SCREEN, pygame.Color(color), sprite.rect, thickness)


def shift_sprite(sprite, verdict):
    if 'top' in verdict[0]:
        sprite.moving_rect[1] += verdict[1]
        if sprite.collider is not None:
            sprite.collider.moving_rect[1] += verdict[1]
    elif 'bottom' in verdict[0]:
        sprite.moving_rect[1] -= verdict[1]
        if sprite.collider is not None:
            sprite.collider.moving_rect[1] -= verdict[1]
    if 'left' in verdict[0]:
        sprite.moving_rect[0] += verdict[1]
        if sprite.collider is not None:
            sprite.collider.moving_rect[0] -= verdict[1]
    elif 'right' in verdict[0]:
        sprite.moving_rect[0] -= verdict[1]
        if sprite.collider is not None:
            sprite.collider.moving_rect[0] -= verdict[1]

    sprite.rect = pygame.Rect(sprite.moving_rect)
    if sprite.collider is not None:
        sprite.collider.rect = pygame.Rect(sprite.collider.moving_rect)


def check_colliders(moving_colliders, static_colliders, frame_tick, clearing=False, camera=None, location_groups=None):
    global previous_collide_verdicts
    current_verdicts = []
    moving_colliders_iterator = 0

    if clearing:
        previous_collide_verdicts = []

    for moving_collider in moving_colliders.get_sprites():
        moving_verdicts = []
        static_colliders_iterator = 0

        for static_collider in static_colliders.get_sprites():
            verdict = moving_collider.check_possible_collide_side(static_collider, frame_tick)
            moving_verdicts.append(verdict)

            if not moving_collider.check_x_axis_intersection(static_collider) and \
                    previous_collide_verdicts:
                if previous_collide_verdicts[moving_colliders_iterator][static_colliders_iterator] is not None:
                    if 'bottom' in \
                            previous_collide_verdicts[moving_colliders_iterator][static_colliders_iterator][0]:
                        if camera is None:
                            unblock_side(moving_collider.owner, 'bottom')
                        else:
                            unblock_side(camera, 'bottom')
                    elif 'top' in \
                            previous_collide_verdicts[moving_colliders_iterator][static_colliders_iterator][0]:
                        if camera is None:
                            unblock_side(moving_collider.owner, 'top')
                        else:
                            unblock_side(camera, 'top')
            if not moving_collider.check_y_axis_intersection(static_collider) and \
                    previous_collide_verdicts:
                if previous_collide_verdicts[moving_colliders_iterator][static_colliders_iterator] is not None:
                    if 'right' in \
                            previous_collide_verdicts[moving_colliders_iterator][static_colliders_iterator][0]:
                        if camera is None:
                            unblock_side(moving_collider.owner, 'right')
                        else:
                            unblock_side(camera, 'right')
                    elif 'left' in \
                            previous_collide_verdicts[moving_colliders_iterator][static_colliders_iterator][0]:
                        if camera is None:
                            unblock_side(moving_collider.owner, 'left')
                        else:
                            unblock_side(camera, 'left')

            if verdict is not None:
                if len(verdict) == 2:
                    if camera is None:
                        moving_collider.make_collide(verdict[0], verdict[1])
                    else:
                        for location_group in location_groups:
                            for sprite in location_group.get_sprites():
                                # print(sprite.collider)
                                # print(moving_collider)
                                # print('--------------------------------')
                                if sprite.collider == moving_collider:
                                    moving_collider.make_collide(verdict[0], verdict[1], camera=camera)
                                else:
                                    #print(verdict[1])
                                    shift_sprite(sprite, verdict)
                elif len(verdict) == 3:
                    if camera is None:
                        moving_collider.make_collide(verdict[0], verdict[1], blocked_sides=verdict[2])
                    else:
                        for location_group in location_groups:
                            for sprite in location_group.get_sprites():
                                if sprite.collider == moving_collider:
                                    moving_collider.make_collide(verdict[0], verdict[1], blocked_sides=verdict[2],
                                                                 camera=camera)
                                else:
                                    shift_sprite(sprite, verdict)

            static_colliders_iterator += 1

        current_verdicts.append(moving_verdicts)
        moving_colliders_iterator += 1

    previous_collide_verdicts = current_verdicts.copy()