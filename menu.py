import pygame
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)

    return image


pygame.init()

WIDTH = 900
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))

clock = pygame.time.Clock()

menu_buttons = pygame.sprite.Group()

# создадим спрайт
button_start = pygame.sprite.Sprite()
# определим его вид
button_start.image = load_image("button_start_game.png")
# и размеры
button_start.rect = button_start.image.get_rect()
button_start.rect.x = WIDTH // 2 - button_start.rect[2] // 2
button_start.rect.y = 200

# создадим спрайт
button_exit = pygame.sprite.Sprite()
# определим его вид
button_exit.image = load_image("button_exit.png")
# и размеры
button_exit.rect = button_start.image.get_rect()
button_exit.rect.x = WIDTH // 2 - button_start.rect[2] // 2
button_exit.rect.y = 600

# создадим спрайт
button_settings = pygame.sprite.Sprite()
# определим его вид
button_settings.image = load_image("button_settings.png")
# и размеры
button_settings.rect = button_start.image.get_rect()
button_settings.rect.x = WIDTH // 2 - button_start.rect[2] // 2
button_settings.rect.y = 400

menu_buttons.add(button_start)
menu_buttons.add(button_settings)
menu_buttons.add(button_exit)

game_started = False

running = True
while running:

    if not game_started:

        # игра еще не началась

        clock.tick(60)
        screen.fill((255, 255, 255))

        menu_buttons.draw(screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if (button_start.rect.x <= event.pos[0] <= button_start.rect.x + button_start.rect[2]) and (
                        button_start.rect.y <= event.pos[1] <= button_start.rect.y + button_start.rect[3]):
                    
                    game_started = True

                elif (button_exit.rect.x <= event.pos[0] <= button_exit.rect.x + button_exit.rect[2]) and (
                        button_exit.rect.y <= event.pos[1] <= button_exit.rect.y + button_exit.rect[3]):
                    running = False

    elif game_started:
        # игра началасб

        screen.fill((0, 0, 0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

    pygame.display.flip()
