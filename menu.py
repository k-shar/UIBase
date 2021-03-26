import pygame
from constants import *
from window_sizing import Window


def menu(screen):
    clock = pygame.time.Clock()
    pygame.display.set_caption("Menu Screen")
    square = Window((10, 10))

    while True:
        screen.fill(RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return screen
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    pygame.display.init()
    main_screen = pygame.display.set_mode((300, 200), pygame.RESIZABLE)
    menu(main_screen)
    pygame.quit()
