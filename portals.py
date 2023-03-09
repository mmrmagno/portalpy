import pygame

class Blue_Portal(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.image.fill('blue')
        # self.image = pygame.image.load("assets/portals/h_blue_portal.png").convert()
        # self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect(bottomleft = pos)

    def update(self,x_shift):
        self.rect.x += x_shift

class Orange_Portal(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((64, 8))
        self.image.fill('orange')
        # self.image = pygame.image.load("assets/portals/h_orange_portal.png").convert()
        # self.image = pygame.transform.rotate(self.image, 290)
        self.rect = self.image.get_rect(topleft = pos)

    def update(self,x_shift):
        self.rect.x += x_shift