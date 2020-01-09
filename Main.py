import pygame
import sys
from constants import WIDTH, HEIGHT, FPS
from Player import Player
from Camera import Camera
from Background import Background


class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.entities = pygame.sprite.Group()

    def terminate_game(self):
        pygame.quit()
        sys.exit()

    def start_game(self):
        background = Background(self.entities, 'Grass background.jpg', 100, -300)
        player = Player(self.entities, 0, 0, 250)
        player.moving_rect[0] = WIDTH / 2 - player.rect.w / 2
        player.moving_rect[1] = HEIGHT / 2 - player.rect.h / 2
        camera = Camera()

        while True:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate_game()

            camera.update(player)
            for entity in self.entities:
                camera.apply(entity)

            self.entities.update()
            self.entities.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)