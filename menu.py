import pygame
from constants import *
from window_sizing import Window


def menu(screen):
    clock = pygame.time.Clock()
    pygame.display.set_caption("Menu Screen")

    window = Window((100, 100), GREEN, (0.9, 0.9), (0.5, 0.5), screen)
    pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE, {'size': (500, 300), 'w': 500, 'h': 300}))

    while True:
        screen.fill(RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return screen
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                window.resize()

        window.draw()

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    pygame.display.init()
    main_screen = pygame.display.set_mode((300, 200), pygame.RESIZABLE)
    menu(main_screen)
    pygame.quit()
