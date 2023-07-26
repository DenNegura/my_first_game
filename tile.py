from settings import Settings
from sprite_sheet import SpriteSheet

class Tile:

    TILE = "tile"

    SRITE = (TILE, "sprite")

    SIZE = ((TILE, "size", "width"), (TILE, "size", "height"))

    DELAY = (TILE, "delay")

    def __init__(self, settings: Settings, name: str):
        self._settings = settings
        self._name = name

        self._sprite_path = self._settings.get(self._path(self.SRITE, self._name))
        self._size = self._settings.get(self._path(self.SIZE, self._name))
        self._delay = self._settings.get(self._path(self.DELAY, self._name))

        self._sheet = SpriteSheet(self._sprite_path, self._size)

    def get_name(self):
        return self._name

    def _path(self, path: tuple | list, property: str) -> tuple:
        _path = []
        if type(path[0]) == tuple or type(path[0]) == list:
            for part_path in path:
                _part_path = list(part_path)
                _part_path.append(property)
                _path.append(_part_path)
        else:
            _path = list(path)
            _path.append(property)
        return tuple(_path)