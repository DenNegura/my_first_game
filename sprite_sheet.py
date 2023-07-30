import pygame


class SpriteSheet:

    def __init__(self, sprite_list: pygame.Surface | str, tile_size: tuple):
        if type(sprite_list) == str:
            self._sheet = pygame.image.load(sprite_list)
        self._tile_size = tile_size

    def get_tile(self, row: int, col: int,
                 padding: tuple[int, int, int, int] | tuple[int, int] | int = 0) -> pygame.Surface:
        x = col * self._tile_size[0]
        y = row * self._tile_size[1]
        rect = pygame.Rect(x, y, self._tile_size[0], self._tile_size[1])
        tile = pygame.Surface((self._tile_size[0], self._tile_size[1]), pygame.SRCALPHA)
        tile.blit(self._sheet, (0, 0), rect)
        return tile

    def get_tile_size(self):
        return self._tile_size
