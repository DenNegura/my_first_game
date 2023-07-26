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

    SIDE = ["top", "right", "left", "bottom"]

    DIRECTION = ["idle", "walk", "run"]

    PATH = [["actor", "direction", "", "state", "", "position", "row"],
            ["actor", "direction", "", "state", "", "position", "col"]]

    def __init__(self, settings: Settings, name: str):
        super().__init__(settings, name)

        self._tiles = {}

    def _init_tiles(self):
        pass
