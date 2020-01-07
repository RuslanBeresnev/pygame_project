import pygame
import sys
from constants import FPS, WIDTH, HEIGHT
from Player import Player
from Camera import Camera
from Background import Background


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.clock = pygame.time.Clock()
        self.entitys = pygame.sprite.Group()

        self.start_game()

    def terminate_game(self):
        pygame.quit()
        sys.exit()

    def start_game(self):
        background = Background(self.entitys, 'Фон с травой.jpg', -300, -300)
        player = Player(self.entitys, 200, 200, 250)
        camera = Camera()

        while True:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate_game()

            camera.update(player)
            for entity in self.entitys:
                camera.apply(entity)

            self.entitys.update()
            self.entitys.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)


game = Main()