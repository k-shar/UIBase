import pygame


class Window:
    def __init__(self, size: tuple):
        self.image = pygame.Surface(size)
