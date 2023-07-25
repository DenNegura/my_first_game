import pygame
from pygame.sprite import Sprite

from actor import Actor
from settings import Settings
from sprite_sheet import SpriteSheet


class Hero(Actor, Sprite):

    NAME = "hero"

    SPRITE_PATH = ("hero", "sprite")

    SIZE = (("hero", "size", "width"), ("hero", "size", "height"))

    DELAY = ("hero", "delay")

    DIRECTION = ("top", "right", "down", "left")

    STATE = ("idle", "walk", "run")

    DETAIL = ("row", "start", "count")

    def __init__(self):
        super(Hero, self).__init__(self.NAME)
        Sprite.__init__(self)
        self._read_properties()
        self._sheet = SpriteSheet(self._sprite_path, self._size)
        self._frame = 0
        self._timer = 0
        self._load_tiles()

    def _read_properties(self):
        self._settings = Settings()
        self._sprite_path = self._settings.get(self.SPRITE_PATH)
        self._size = self._settings.get(self.SIZE)
        self._delay = self._settings.get(self.DELAY)

    def _load_tiles(self):
        pass


    def idle(self, time):
        self._timer += time
        if self._timer > self._delay:
            self._timer = 0
            self._frame += 1
            return self._sheet.get_tile(2, self._frame % 8)
        return self._sheet.get_tile(2, self._frame % 8)


hero = Hero()

screen = pygame.display.set_mode((800, 600))
running = True
clock = pygame.time.Clock()  # Создаем объект для отслеживания времени
while running:
    dt = clock.tick(60)  # Ограничиваем FPS до 60 и получаем прошедшее время с момента последнего вызова clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновляем анимацию героя
    hero_tile = hero.idle(dt)

    screen.fill((0, 0, 0))
    # Отрисовываем текущий тайл анимации героя на экране
    screen.blit(hero_tile, (100, 100))
    pygame.display.flip()

pygame.quit()
