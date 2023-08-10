import sys


class Map:

    def __init__(self):
        self._map = {}
        self._history = []

    def set(self, x: int, y: int, tile: int):
        self._add(x, y, tile)
        self._history.append((x, y, tile))

    def _add(self, x: int, y: int, tile):
        y_map = self._map.get(x)
        if y_map:
            y_map[y] = tile

        else:
            self._map[x] = {y: tile}

    def remove(self, x: int, y: int):
        y_map = self._map.get(x)
        if y_map:
            return y_map.pop(y, default=None)
        else:
            return None

    def undo(self) -> tuple:
        self._history.pop()
        if self._history:
            self._add(*self._history.pop())
