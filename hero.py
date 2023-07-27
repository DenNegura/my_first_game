import pygame
from pygame.sprite import Sprite

from actor import Actor
from settings import Settings


class Hero(Actor, Sprite):

    def __init__(self, name):
        super(Hero, self).__init__(Settings(), name)
        Sprite.__init__(self)
        self._frame = 0
        self._timer = 0
        self.image = self.get_tile(self.BOTTOM, self.IDLE, 0)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200

    def idle(self, time):
        self._timer += time
        if self._timer > self._delay:
            self._timer = 0
            self._frame += 1
            if self._frame > 3:
                self._frame = 0

            return self.get_tile(self.LEFT, self.WALK, self._frame)
        return self.get_tile(self.LEFT, self.WALK, self._frame)


# def move_hero(self, hero: Hero):
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         hero.to_left()
#     if keys[pygame.K_RIGHT]:
#         hero.to_right()
#     if keys[pygame.K_UP]:
#         hero.to_up()
#     if keys[pygame.K_DOWN]:
#         hero.to_down()


hero = Hero("hero")
all_sprites = pygame.sprite.Group()
all_sprites.add(hero)

screen = pygame.display.set_mode((800, 600))
running = True
clock = pygame.time.Clock()  # Создаем объект для отслеживания времени

while running:
    dt = clock.tick(60)  # Ограничиваем FPS до 60 и получаем прошедшее время с момента последнего вызова clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновляем анимацию героя
    # hero_tile = hero.idle(dt)
    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    # Отрисовываем текущий тайл анимации героя на экране
    # screen.blit(hero_tile, (100, 100))
    pygame.display.flip()

pygame.quit()
