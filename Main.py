import pygame
import sys
from constants import WIDTH, HEIGHT, SCREEN, COLLIDERS_CONTOUR
from functions import set_objects_ticks
from Group import Group
from Player import Player
from Camera import Camera
from Location import Location
from functions import draw_group_contour, check_colliders, determine_direction


class Main:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.frame_tick = None
        self.previous_collide_verdicts = []

        self.entities = Group()
        self.location_cells = Group()
        self.location_objects = Group()
        self.moving_colliders = Group()
        self.static_colliders = Group()

    def terminate_game(self):
        pygame.quit()
        sys.exit()

    def start_game(self):
        player_spawn_x = WIDTH / 2.13
        player_spawn_y = HEIGHT / 2.25
        player = Player(self.entities, self.moving_colliders, player_spawn_x, player_spawn_y, 100, 300)

        sheet = Location('Surface map.txt', self.location_cells, 'surface', 0, 0, player.speed, collider_group=None)
        sheet.location_creating()
        terrain = Location('Terrain map.txt', self.location_objects, 'terrain', 0, 0, player.speed,
                           collider_group=self.static_colliders, sheet=sheet)
        terrain.location_creating()

        camera = Camera()
        previous_camera_works = False

        while True:
            self.frame_tick = self.clock.tick() / 1000
            set_objects_ticks(self.frame_tick, player, camera)
            determine_direction(player)
            SCREEN.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate_game()

            camera_works = camera.update(player)

            if not camera_works:
                if not previous_camera_works:
                    check_colliders(self.moving_colliders, self.static_colliders, self.frame_tick)
                else:
                    check_colliders(self.moving_colliders, self.static_colliders, self.frame_tick, clearing=True)
            else:
                if previous_camera_works:
                    check_colliders(self.static_colliders, self.moving_colliders, self.frame_tick, camera=camera,
                                    location_groups=[self.location_cells, self.location_objects])
                else:
                    check_colliders(self.static_colliders, self.moving_colliders, self.frame_tick, clearing=True,
                                    camera=camera, location_groups=[self.location_cells, self.location_objects])

            previous_camera_works = camera_works

            for cell in self.location_cells.get_sprites():
                camera.apply(cell)
            for obj in self.location_objects.get_sprites():
                camera.apply(obj)

            self.location_cells.draw(SCREEN)
            self.entities.update()
            self.entities.draw(SCREEN)
            self.location_objects.draw(SCREEN)

            if COLLIDERS_CONTOUR:
                draw_group_contour(self.moving_colliders, 'red', 2)
                draw_group_contour(self.static_colliders, 'red', 2)

            pygame.display.flip()