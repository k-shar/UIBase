import pygame
from constants import *
from window_sizing import ScaleWindow, AspectWindow


def menu(screen):
    clock = pygame.time.Clock()
    pygame.display.set_caption("Menu Screen")

    # define Window elements
    window = AspectWindow(BLUE, (16, 9), (0.5, 0.5), 1)
    game_space = AspectWindow(GREEN, (1, 1), (4.5/16, 0.5), 0.9)
    title = AspectWindow(WHITE, (7, 9), (12.5/16, 0.5), 0.8)

    flag = 0
    pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE, {'w': 500, 'h': 300}))
    while True:
        screen.fill(RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return screen
            if event.type == pygame.VIDEORESIZE:

                # resize largest to smallest, as to pass in the new resized parent surf
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                window.resize(screen)
                game_space.resize(window.image)
                title.resize(window.image)

        # blit the child surface onto the parent surface, at a position relative to the parent
        screen.blit(window.image, (window.rect.x, window.rect.y))

        if flag % 2 == 0:
            window.image.blit(game_space.image, (game_space.rect.x, game_space.rect.y))
            window.image.blit(title.image, (title.rect.x, title.rect.y))
            flag += 1
        else:
            window.image.blit(title.image, (title.rect.x, title.rect.y))
            window.image.blit(game_space.image, (game_space.rect.x, game_space.rect.y))
            flag += 1

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    pygame.display.init()
    main_screen = pygame.display.set_mode((300, 200), pygame.RESIZABLE)
    menu(main_screen)
    pygame.quit()
