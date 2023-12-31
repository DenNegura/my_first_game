from settings import Settings


class Tile:

    def __init__(self, settings: Settings, name: str):
        self._settings = settings
        self._name = name
        self._position = (0, 0)

        self._sprite_path = self._settings.get(self._name, self._settings.Tile.SPRITE)
        self._size = self._settings.get(self._name, self._settings.Tile.SIZE)
        self._delay = self._settings.get(self._name, self._settings.Tile.DELAY)
