import pygame
from Button import Button
from constants import WIDTH, HEIGHT
from Main import Main
from functions import load_image


class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.buttons = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

        self.menu_creating()

    def menu_creating(self):
        background_width = WIDTH
        background_height = int(WIDTH // 1.777)
        background_image = pygame.transform.scale(load_image('Menu background.jpg'), (background_width,
                                                                                      background_height))

        logo_width = int(WIDTH * 0.75)
        logo_height = int(WIDTH * 0.09)
        logo_x = WIDTH // 2 - logo_width // 2
        logo_y = HEIGHT // 7.2
        logo_image = pygame.transform.scale(load_image('Detventure logo.png'), (logo_width, logo_height))

        buttons_width = WIDTH // 3.2
        buttons_height = WIDTH // 16
        start_button_x, start_button_y = WIDTH // 2 - buttons_width // 2, HEIGHT // 2.25
        start_button = Button(self.buttons, 'Start game button.png', start_button_x, start_button_y,
                              buttons_width, buttons_height)
        settings_button_x, settings_button_y = WIDTH // 2 - buttons_width // 2, HEIGHT // 1.64
        settings_button = Button(self.buttons, 'Settings button.png', settings_button_x, settings_button_y,
                                 buttons_width, buttons_height)
        exit_button_x, exit_button_y = WIDTH // 2 - buttons_width // 2, HEIGHT // 1.29
        exit_button = Button(self.buttons, 'Exit game button.png', exit_button_x, exit_button_y,
                             buttons_width, buttons_height)

        game = Main()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if exit_button.rect.collidepoint(event.pos):
                        game.terminate_game()
                    elif start_button.rect.collidepoint(event.pos):
                        game.start_game()
                    elif settings_button.rect.collidepoint(event.pos):
                        pass

            self.screen.blit(background_image, (0, 0))
            self.screen.blit(logo_image, (logo_x, logo_y))
            self.buttons.draw(self.screen)
            pygame.display.flip()


menu = Menu()