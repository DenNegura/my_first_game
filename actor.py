from settings import Settings
from tile import Tile


class Actor(Tile):
    class Direction:
        TOP = 0

        RIGHT = 1

        LEFT = 2

        BOTTOM = 3

    class State:
        IDLE = 1

        WALK = 2

        RUN = 3

    SIDES = ["top", "right", "left", "bottom"]

    DIRECTIONS = ["idle", "walk", "run"]

    ACTOR = "actor"

    def __init__(self, settings: Settings, name: str):
        super().__init__(settings, name)

        self._tiles = {}
        self._init_tiles()

    def _init_tiles(self):
        for side in self.SIDES:
            for direction in self.DIRECTIONS:
                self._tiles[side] = {direction: self.ACTOR}

actor = Actor(Settings(), "hero")
print(actor._tiles)