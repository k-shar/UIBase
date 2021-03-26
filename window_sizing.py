import pygame


class Window:
    def __init__(self, size: tuple, color):

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def resize(self, parent):
        size = (int(parent.get_size()[0] * 0.5), int(parent.get_size()[1] * 0.5))
        self.image = pygame.transform.scale(self.image, size)

        self.rect = self.image.get_rect()
        self.rect.centerx = parent.get_width() * 0.5
        self.rect.centery = parent.get_height() * 0.5
