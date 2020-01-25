import pygame
import sys
from constants import WIDTH, HEIGHT
from functions import set_objects_ticks
from Player import Player
from Camera import Camera
from Location import Location


class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

        self.entities = pygame.sprite.Group()
        self.location_cells = pygame.sprite.Group()

    def terminate_game(self):
        pygame.quit()
        sys.exit()

    def start_game(self):
        world = Location('World map.txt', self.location_cells, 0, 0)
        world.location_creating()

        player = Player(self.entities, 0, 0, 300)
        player.moving_rect[0] = WIDTH / 2 - player.rect.w / 2
        player.moving_rect[1] = HEIGHT / 2 - player.rect.h / 2

        camera = Camera()

        while True:
            tick = self.clock.tick() / 1000
            set_objects_ticks(tick, player, camera)
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate_game()

            camera.update(player)
            for cell in self.location_cells:
                camera.apply(cell)

            self.location_cells.draw(self.screen)
            self.entities.update()
            self.entities.draw(self.screen)

            pygame.display.flip()