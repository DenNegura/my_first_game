from settings import Settings
from sprite_sheet import SpriteSheet


class Tile:

    def __init__(self, settings: Settings, name: str):
        self._settings = settings
        self._name = name
        self._position = (0, 0)

        self._sprite_path = self._settings.get(self._name, self._settings.Tile.SPRITE)
        self._size = self._settings.get(self._name, self._settings.Tile.SIZE)
        self._delay = self._settings.get(self._name, self._settings.Tile.DELAY)

    def get_name(self):
        return self._name
