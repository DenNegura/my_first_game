import pygame

from hero import Hero
from sprite_sheet import SpriteSheet
from сharacter import Character


class Game:
    _WINDOW_WIDTH = 840

    _WINDOW_HEIGHT = 600

    def __init__(self):
        self.size = self._WINDOW_WIDTH, self._WINDOW_HEIGHT
        self._running = False
        self._display_surf = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("game")
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.on_init()

        tiles = SpriteSheet("./asserts/tiles_img.png", (32, 32))
        hero = Hero("hero")
        # sprites = pygame.sprite.Group(hero.idle(10))
        clock = pygame.time.Clock()
        while self._running:
            dt = clock.tick(60)
            for event in pygame.event.get():
                self.on_event(event)
                self.create_background(tiles)
                # self.move_character(character)
                # sprites.draw(self._display_surf)
                self._display_surf.blit(hero.idle(dt), (100, 100))
                pygame.display.flip()
        self.on_cleanup()

    def create_background(self, tiles):
        size = 32
        for x in range(0, self._WINDOW_WIDTH, size):
            for y in range(0, self._WINDOW_HEIGHT, size):
                self._display_surf.blit(tiles.get_tile(3, 6), (x, y))

    def move_character(self, character: Character):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character.to_left()
        if keys[pygame.K_RIGHT]:
            character.to_right()
        if keys[pygame.K_UP]:
            character.to_up()
        if keys[pygame.K_DOWN]:
            character.to_down()
