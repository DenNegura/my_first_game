import direction
import pygame
import state
from settings import Settings
from sprite_sheet import SpriteSheet
from tile import Tile


class Actor(Tile, pygame.sprite.Sprite):

    def __init__(self, name: str, settings: Settings, position: tuple | list):
        super().__init__(settings, name)
        pygame.sprite.Sprite.__init__(self)
        self._sheet = SpriteSheet(self._sprite_path, self._size)
        self.image = self._init_state()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self._tile_dict = self._init_tiles()
        self._speed_dict = self._read_speed()
        self._use_tile_set = self.get_tile_set(direction.BOTTOM, state.IDLE)
        self._frame = 0
        self._update_time = 0

    def update(self):
        ticks = pygame.time.get_ticks()
        if ticks - self._delay > self._update_time:
            self._update_time = ticks
            self._frame += 1
            if self._frame == len(self._use_tile_set):
                self._frame = 0
            self.image = self._use_tile_set[self._frame]
            x, y = self.rect.x, self.rect.y
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = x, y
            self.move(self._direction, self._state)

    def _init_state(self) -> pygame.Surface:
        init_state = self._settings.get(self._name, self._settings.Actor.STATE)
        return self._sheet.get_tile(*init_state)

    def _read_speed(self) -> dict[int]:
        speed = {}
        for _state in state.STATES:
            speed[_state] = self._settings.get(self._name, self._settings.Actor.SPEED, _state.get())
        return speed

    def _init_tiles(self) -> dict:
        _tile_dict = {}
        for _direction in direction.DIRECTIONS:
            direction_dict = {}
            for _state in state.STATES:
                direction_dict[_state] = self._read_tiles(_direction, _state)
            _tile_dict[_direction] = direction_dict
        return _tile_dict

    def _read_tiles(self, direction: direction.Direction, state: state.State):
        tiles_coords = self._settings.get(self.get_name(), direction.get(), state.get())
        return [self._sheet.get_tile(row, col) for row, col in tiles_coords]

    def set_position(self, coords):
        self.rect.x, self.rect.y = coords

    def move(self, direction: direction.Direction, state: state.State):
        self.set_position(direction.change(self.rect.x, self.rect.y, self._speed_dict[state]))

    def get_directions(self) -> tuple[direction.Direction]:
        return tuple(self._tile_dict.keys())

    def get_states(self, direction: direction.Direction) -> tuple[state.State]:
        return tuple(self._tile_dict[direction].keys())

    def get_tile(self, direction: direction.Direction, state: state.State, index):
        return self.get_tile_set(direction, state)[index]

    def get_tile_set(self, direction: direction.Direction, state: state.State) -> list[pygame.Surface]:
        return self._tile_dict[direction][state]
