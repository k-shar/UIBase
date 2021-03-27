import pygame


class ScaleWindow:
    def __init__(self, color, size_relative_to_parent: tuple, pos_relative_to_parent: tuple):

        # create surface and rect with some arbitrary non-zero size
        self.image = pygame.Surface((1, 1))
        self.rect = self.image.get_rect()

        # color in the surface, this would not work if surface was of size (0, 0)
        self.color = color
        self.image.fill(self.color)

        # define the relative scale of the window
        self.rel_pos = pos_relative_to_parent
        self.rel_size = size_relative_to_parent

    def resize(self, parent: pygame.Surface):
        self.image.fill(self.color)
        
        # new size is a fraction of the parents size
        size = (int(parent.get_size()[0] * self.rel_size[0]), int(parent.get_size()[1] * self.rel_size[1]))
        # scale surface to this new size
        self.image = pygame.transform.scale(self.image, size)

        # create new rect
        self.rect = self.image.get_rect()
        # position of rect is some fraction of the parents size relative to the parent surface
        self.rect.centerx = parent.get_size()[0] * self.rel_pos[0]
        self.rect.centery = parent.get_size()[1] * self.rel_pos[1]



class AspectWindow:
    def __init__(self):
        pass

