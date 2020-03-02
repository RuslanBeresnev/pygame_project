import pygame
from functions import block_side


class Collider(pygame.sprite.Sprite):
    def __init__(self, group, owner, indent_x, indent_y, width, height, trigger=False):
        super().__init__()
        group.add(self)
        self.owner = owner
        self.indent_x = indent_x
        self.indent_y = indent_y
        self.trigger = trigger

        self.moving_rect = [self.owner.rect.x + self.indent_x, self.owner.rect.y + self.indent_y,
                            width, height]
        self.rect = pygame.Rect(self.moving_rect)

    def check_x_axis_intersection(self, second_collider):
        if second_collider.rect.y < self.rect.y + self.rect.height < second_collider.rect.y + \
                second_collider.rect.height or self.rect.y < second_collider.rect.y + \
                second_collider.rect.height < self.rect.y + self.rect.height or \
                (self.rect.y > second_collider.rect.y and self.rect.y +
                 self.rect.height < second_collider.rect.y + second_collider.rect.height) or \
                (second_collider.rect.y > self.rect.y and second_collider.rect.y +
                 second_collider.rect.height < self.rect.y + self.rect.height):
            return True
        else:
            return False

    def check_y_axis_intersection(self, second_collider):
        if second_collider.rect.x < self.rect.x + self.rect.width < second_collider.rect.x + \
                second_collider.rect.width or self.rect.x < second_collider.rect.x + \
                second_collider.rect.width < self.rect.x + self.rect.width or \
                (self.rect.x > second_collider.rect.x and self.rect.x +
                 self.rect.width < second_collider.rect.x + second_collider.rect.width) or \
                (second_collider.rect.x > self.rect.x and second_collider.rect.x +
                 second_collider.rect.width < self.rect.x + self.rect.width):
            return True
        else:
            return False

    def check_possible_collide_side(self, other_collider, frame_tick):
        shift_direction = None
        distance = None
        blocked_sides = None

        if self.check_x_axis_intersection(other_collider):
            if other_collider.rect.x + other_collider.rect.width <= self.rect.x:
                shift_direction = ['left']
                distance = self.rect.x - other_collider.rect.x - other_collider.rect.width
            elif self.rect.x + self.rect.width <= other_collider.rect.x:
                shift_direction = ['right']
                distance = other_collider.rect.x - self.rect.x - self.rect.width
        elif self.check_y_axis_intersection(other_collider):
            if self.rect.y + self.rect.height <= other_collider.rect.y:
                shift_direction = ['bottom']
                distance = other_collider.rect.y - self.rect.y - self.rect.height
            elif other_collider.rect.y + other_collider.rect.height <= self.rect.y:
                shift_direction = ['top']
                distance = self.rect.y - other_collider.rect.y - other_collider.rect.height

        if not self.check_x_axis_intersection(other_collider) and not self.check_y_axis_intersection(other_collider):
            delta_x = None
            delta_y = None

            if self.rect.x >= other_collider.rect.x + other_collider.rect.width and \
                    self.rect.y >= other_collider.rect.y + other_collider.rect.height:
                shift_direction = ['left', 'top']
                delta_x = self.rect.x - other_collider.rect.x - other_collider.rect.width
                delta_y = self.rect.y - other_collider.rect.y - other_collider.rect.height
            elif self.rect.x >= other_collider.rect.x + other_collider.rect.width and \
                    self.rect.y + self.rect.height <= other_collider.rect.y:
                shift_direction = ['left', 'bottom']
                delta_x = self.rect.x - other_collider.rect.x - other_collider.rect.width
                delta_y = other_collider.rect.y - self.rect.y - self.rect.height
            elif other_collider.rect.x >= self.rect.x + self.rect.width and \
                    other_collider.rect.y >= self.rect.y + self.rect.height:
                shift_direction = ['right', 'bottom']
                delta_x = other_collider.rect.x - self.rect.x - self.rect.width
                delta_y = other_collider.rect.y - self.rect.y - self.rect.height
            elif other_collider.rect.x >= self.rect.x + self.rect.width and \
                    other_collider.rect.y + other_collider.rect.height <= self.rect.y:
                shift_direction = ['right', 'top']
                delta_x = other_collider.rect.x - self.rect.x - self.rect.width
                delta_y = self.rect.y - other_collider.rect.y - other_collider.rect.height

            if delta_x is not None and delta_y is not None:
                if delta_y >= delta_x:
                    distance = delta_y
                    if 'top' in shift_direction:
                        blocked_sides = ['top']
                    elif 'bottom' in shift_direction:
                        blocked_sides = ['bottom']
                elif delta_y < delta_x:
                    distance = delta_x
                    if 'left' in shift_direction:
                        blocked_sides = ['left']
                    elif 'right' in shift_direction:
                        blocked_sides = ['right']

        if shift_direction and distance is not None:
            if self.owner.speed * frame_tick > distance:
                if blocked_sides is not None:
                    return (shift_direction, distance, blocked_sides)
                else:
                    return (shift_direction, distance)
            else:
                return None

    def make_collide(self, shift_direction, distance, blocked_sides=None, camera=None):
        make_shift = True
        for direction in shift_direction:
            if camera is None:
                if direction not in self.owner.direction_sides:
                    make_shift = False
                    break
            else:
                if direction not in camera.direction_sides:
                    make_shift = False
                    break

        if make_shift:
            if 'left' in shift_direction:
                self.owner.moving_rect[0] -= distance
                self.moving_rect[0] -= distance
            if 'right' in shift_direction:
                self.owner.moving_rect[0] += distance
                self.moving_rect[0] += distance
            if 'bottom' in shift_direction:
                self.owner.moving_rect[1] += distance
                self.moving_rect[1] += distance
            if 'top' in shift_direction:
                self.owner.moving_rect[1] -= distance
                self.moving_rect[1] -= distance

            self.owner.rect = pygame.Rect(self.owner.moving_rect)
            self.rect = pygame.Rect(self.moving_rect)

            if not self.trigger:
                if blocked_sides is not None:
                    for side in blocked_sides:
                        if camera is None:
                            block_side(self.owner, side)
                        else:
                            block_side(camera, side)
                else:
                    for side in shift_direction:
                        if camera is None:
                            block_side(self.owner, side)
                        else:
                            block_side(camera, side)
            else:
                self.owner.in_collide()