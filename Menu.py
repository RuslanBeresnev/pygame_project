import pygame
from Button import Button
from constants import WIDTH, FPS
from Main import Main


class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.buttons = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

        self.menu_creating()

    def menu_creating(self):
        buttons_width = 600
        buttons_height = 150

        start_button = Button(self.buttons, 'Start game button.png', WIDTH // 2 - buttons_width // 2, 200,
                              buttons_width, buttons_height)
        exit_button = Button(self.buttons, 'Exit game button.png', WIDTH // 2 - buttons_width // 2, 600,
                             buttons_width, buttons_height)
        settings_button = Button(self.buttons, 'Settings button.png', WIDTH // 2 - buttons_width // 2, 400,
                                 buttons_width, buttons_height)

        game = Main()

        while True:
            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_button.rect.collidepoint(event.pos):
                        game.terminate_game()
                    elif start_button.rect.collidepoint(event.pos):
                        game.start_game()
                    elif settings_button.rect.collidepoint(event.pos):
                        pass

            self.buttons.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)


menu = Menu()