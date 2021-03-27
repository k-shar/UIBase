import pygame
from constants import *
from window_sizing import ScaleWindow, AspectWindow


def menu(screen):
    clock = pygame.time.Clock()
    pygame.display.set_caption("Menu Screen")

    # define Window elements
    border = ScaleWindow(GREEN, (0.9, 0.9), (0.5, 0.5))
    game_space = AspectWindow(BLUE, (9, 4), 0)
    tile = AspectWindow(WHITE, (16, 9), 0)

    pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE, {'w': 500, 'h': 300}))
    while True:
        screen.fill(RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return screen
            if event.type == pygame.VIDEORESIZE:

                # resize largest to smallest, as to pass in the new resized parent surf
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                border.resize(screen)
                game_space.resize(border.image)
                tile.resize(game_space.image)

        # blit the child surface onto the parent surface, at a position relative to the parent
        screen.blit(border.image, (border.rect.x, border.rect.y))
        border.image.blit(game_space.image, (game_space.rect.x, game_space.rect.y))
        game_space.image.blit(tile.image, (tile.rect.x, tile.rect.y))

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    pygame.display.init()
    main_screen = pygame.display.set_mode((300, 200), pygame.RESIZABLE)
    menu(main_screen)
    pygame.quit()
