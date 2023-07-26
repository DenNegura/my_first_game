from settings import Settings
from sprite_sheet import SpriteSheet


class Tile:

    def __init__(self, settings: Settings, name: str):
        self._settings = settings
        self._name = name
        self._position = (0, 0)

        self._sprite_path = self._settings.get(self._settings.Tile.SPRITE, self._name)
        self._size = self._settings.get(self._settings.Tile.SIZE, self._name)
        self._delay = self._settings.get(self._settings.Tile.DELAY, self._name)
        self._sprite_position = self._settings.get(self._settings.Tile.SPRITE_POSITION, self._name)

        self._sheet = SpriteSheet(self._sprite_path, self._size)

    def get_name(self):
        return self._name
