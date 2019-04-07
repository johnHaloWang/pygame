import pygame, sys

pygame.init()

class Runner(pygame.sprite.Sprite):

    def __init__(self, location):
        self.image = pygame.image.load("runner.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect(location, (10, 10))
        self.x_vel = 7
        self.y_vel = 0
        self.ddown = False
        self.adown = False
        self.spacedown = False

    def update(self, Mask, Image):
        self.move(Mask)
        Image.blit(self.image, self.rect)

    def move(self, Mask):
        if self.adown:
            self.calc_next_pos(Mask)
        if self.ddown:
            self.calc_next_pos(Mask)

    def calc_next_pos(self, Mask):
        if self.test_overlap(Mask, (self.x_vel, self.y_vel)):
            self.adjust_pos(Mask)
            self.rect.x += self.x_vel

    def test_overlap(self, Mask, offset):
        off = (self.rect.x + offset[0], self.rect.y + offset[1])
        return Mask.overlap(self.mask, off)

    def adjust_pos(self, Mask):
        while self.test_overlap(Mask, (self.x_vel, self.y_vel)):
            self.x_vel += (1 if self.adown else -1)

