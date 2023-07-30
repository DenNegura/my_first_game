import pygame

import direction
import state
from Key import KeySet
from actor import Actor
from settings import Settings
from sprite_sheet import SpriteSheet


class Player(Actor):

    def __init__(self, name: str,
                 position: tuple[int, int] | list[int, int],
                 direction: direction.Direction, state: state.State):

        super().__init__(name, Settings(), position)
        self._use_tile_set = self.get_tile_set(direction, state)
        self._direction = direction
        self._state = state

    def change_state(self, direction: direction.Direction, state: state.State):
        self._direction = direction
        self._state = state
        self._use_tile_set = self.get_tile_set(self._direction, self._state)

    def get_direction(self):
        return self._direction

    def listen_keys(self):
        keys = pygame.key.get_pressed()
        _state = state.IDLE
        _direction = self._direction

        if keys[pygame.K_w] or keys[pygame.K_d] \
                or keys[pygame.K_a] or keys[pygame.K_s]:
            if keys[pygame.K_LSHIFT]:
                _state = state.RUN
            else:
                _state = state.WALK
        if keys[pygame.K_w]:
            if keys[pygame.K_d]:
                _direction = direction.TOP_RIGHT
            elif keys[pygame.K_a]:
                _direction = direction.TOP_LEFT
            else:
                _direction = direction.TOP
        elif keys[pygame.K_s]:
            if keys[pygame.K_d]:
                _direction = direction.BOTTOM_RIGHT
            elif keys[pygame.K_a]:
                _direction = direction.BOTTOM_LEFT
            else:
                _direction = direction.BOTTOM
        elif keys[pygame.K_d]:
            _direction = direction.RIGHT
        elif keys[pygame.K_a]:
            _direction = direction.LEFT

        self.change_state(_direction, _state)


hero = Player("player", (200, 200), direction.RIGHT, state.IDLE)
all_sprites = pygame.sprite.Group()
all_sprites.add(hero)

# hero_list = []
# for _ in range(1000):
#     new_hero = Hero("hero", (random.randrange(801), random.randrange(601)))
#     hero_list.append(new_hero)
#     all_sprites.add(new_hero)

screen = pygame.display.set_mode((800, 600))
running = True
clock = pygame.time.Clock()  # Создаем объект для отслеживания времени

sheet = SpriteSheet("./asserts/tiles_img.png", (32, 32))
obj = sheet.get_tile(16, 3)
static_sprites = pygame.sprite.Group()
# static_sprites.add(obj)
def create_background():
    size = 32
    for x in range(0, 800, size):
        for y in range(0, 600, size):
            screen.blit(sheet.get_tile(3, 6), (x, y))

while running:
    # Ограничиваем FPS до 60 и получаем прошедшее время с момента последнего вызова clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    hero.listen_keys()
    # for hero_i in hero_list:
    #     hero_i.listen_keys()
    # Обновляем анимацию героя
    # hero_tile = hero.idle(dt)
    create_background()
    all_sprites.draw(screen)

    screen.blit(obj, (400, 400))
    all_sprites.update()
    # Отрисовываем текущий тайл анимации героя на экране
    # screen.blit(hero_tile, (100, 100))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
