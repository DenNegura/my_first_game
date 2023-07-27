from settings import Settings
from sprite_sheet import SpriteSheet
from tile import Tile


class Actor(Tile):
    class Direction:
        def __init__(self, direction: str):
            self._direction = direction

        def get(self):
            return self._direction

    TOP = Direction("top")

    RIGHT = Direction("right")

    LEFT = Direction("left")

    BOTTOM = Direction("bottom")

    _DIRECTIONS = [TOP, RIGHT, LEFT, BOTTOM]

    class State:
        def __init__(self, state: str):
            self._state = state

        def get(self):
            return self._state

    IDLE = State("idle")

    WALK = State("walk")

    RUN = State("run")

    _STATES = [IDLE, WALK, RUN]

    def __init__(self, settings: Settings, name: str):
        super().__init__(settings, name)
        self._sheet = SpriteSheet(self._sprite_path, self._size)
        self._tile_dict = self._init_tiles()

    def _init_tiles(self):
        _tile_dict = {}
        for direction in self._DIRECTIONS:
            direction_dict = {}
            for state in self._STATES:
                direction_dict[state.get()] = self._read_tiles(direction, state)
            _tile_dict[direction.get()] = direction_dict
        return _tile_dict

    def _read_tiles(self, direction: Direction, state: State):
        tiles_coords = self._settings.get(self.get_name(), direction.get(), state.get())
        return [self._sheet.get_tile(row, col) for row, col in tiles_coords]

    def get_tile(self, direction: Direction, state: State, index):
        return self._tile_dict[direction.get()][state.get()][index]


# actor = Actor(Settings(), "hero")
# print(actor.get_tile(actor.LEFT, actor.RUN, 0))
