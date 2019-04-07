import pygame, sys

pygame.init()

class Crate(pygame.sprite.Sprite):
    def __init__(self, location):
        self.image = pygame.image.load("crate.png").convert_alpha()
        self.rect = pygame.Rect(location, (self.image.get_width(), self.image.get_height()))
