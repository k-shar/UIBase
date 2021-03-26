import pygame


class Window:
    def __init__(self, size: tuple, color, scale: tuple, pos: tuple, parent):
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.image.fill(color)

        self.parent = parent
        self.scale = scale
        self.pos = pos

    def resize(self):
        # scale image a fraction of the parents size
        self.rect.width = self.parent.get_width() * self.scale[0]
        self.rect.height = self.parent.get_height() * self.scale[1]
        self.image = pygame.transform.scale(self.image, self.rect.size)

        # align the center of the rect a fraction of the parents size, relative to the parent
        self.rect.centerx = self.parent.get_width() * self.pos[0]
        self.rect.centery = self.parent.get_height() * self.pos[1]
    def draw(self):
        self.parent.blit(self.image, (self.rect.x, self.rect.y))

