import pygame


class ScaleWindow:
    """A Class containing a Surface, that scales to fill a fraction of its parent surface"""
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
        """Resize the surface and the rect's position, to a fraction of the parent (usually ...Window.image)"""
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
    """a Class containing a Surface, that scales to be as large as possible, while maintaining a given aspect ratio"""
    def __init__(self, color, aspect_ratio: tuple, padding: int):

        # create surface and rect with some arbitrary non-zero size
        self.image = pygame.Surface((1, 1))
        self.rect = self.image.get_rect()

        # color in the surface, this would not work if surface was of size (0, 0)
        self.color = color
        self.image.fill(self.color)

        # define aspect ratio and padding
        self.aspect_ratio = aspect_ratio
        # if padding = 0, there *may* be some small overflow
        # if padding = 1, there will never be overflow
        # if padding > 1, padding will shrink the windows size
        self.padding = padding

    def resize(self, parent: pygame.Surface):
        """Resize the surface and the rect's position, maintaining the aspect_ratio"""
        self.image.fill(self.color)

        max_size = parent.get_size()
        current_size = [1, 1]

        # search for the max size we can grow to, while not overflowing parent
        overflown = False
        while not overflown:
            # increase size of image while maintaining aspect ratio
            current_size[0] += self.aspect_ratio[0]
            current_size[1] += self.aspect_ratio[1]

            # if this new size is >= to the size of our container, rollback last change
            if current_size[0] >= max_size[0] or current_size[1] >= max_size[1]:
                # rollback a few times according to padding
                current_size[0] -= self.aspect_ratio[0] * self.padding
                current_size[1] -= self.aspect_ratio[1] * self.padding

                # scale surface and rect to this new found size
                self.image = pygame.transform.scale(self.image, current_size)
                self.rect = self.image.get_rect()

                # set position of rect to be central
                self.rect.centerx = max_size[0] // 2
                self.rect.centery = max_size[1] // 2
                overflown = True





