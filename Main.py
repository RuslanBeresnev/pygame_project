import pygame
import sys
from constants import WIDTH, HEIGHT, SCREEN
from functions import set_objects_ticks
from Group import Group
from Player import Player
from Camera import Camera
from Location import Location


class Main:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.entities = Group()
        self.location_cells = Group()
        self.location_objects = Group()

    def terminate_game(self):
        pygame.quit()
        sys.exit()

    def start_game(self):
        sheet = Location('Surface map.txt', self.location_cells, 'surface', 0, 0)
        sheet.location_creating()
        terrain = Location('Terrain map.txt', self.location_objects, 'terrain', 0, 0, sheet)
        terrain.location_creating()

        player = Player(self.entities, 0, 0, 300)
        player.moving_rect[0] = WIDTH / 2 - player.rect.w / 2
        player.moving_rect[1] = HEIGHT / 2 - player.rect.h / 2

        camera = Camera()

        while True:
            tick = self.clock.tick() / 1000
            set_objects_ticks(tick, player, camera)
            SCREEN.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate_game()

            camera.update(player)
            for cell in self.location_cells.get_sprites():
                camera.apply(cell)
            for obj in self.location_objects.get_sprites():
                camera.apply(obj)

            self.location_cells.draw(SCREEN)
            self.entities.update()
            self.entities.draw(SCREEN)
            self.location_objects.draw(SCREEN)

            pygame.display.flip()