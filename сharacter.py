import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, surface: pygame.Surface, x: int, y: int, speed):
        super().__init__()
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self._speed = speed

    def to_left(self):
        self.rect.x -= self._speed

    def to_right(self):
        self.rect.x += self._speed

    def to_up(self):
        self.rect.y -= self._speed

    def to_down(self):
        self.rect.y += self._speed
