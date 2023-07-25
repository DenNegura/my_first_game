import pygame


class Field(pygame.sprite.Sprite):
    def __init__(self, image):
        self.image = pygame.image.load(image).convert_alpha();
