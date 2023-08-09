import sys


class Map:

    def __init__(self):
        self._map = {}
        self._set_map = set()

    def set(self, x: int, y: int, tile: int):
        self._set_map.add((x, y, tile))
        map = self._map.get(x)
        if map:
            map[y] = tile
        else:
            self._map[x] = {y: tile}
        print(self._map)
        print(self._set_map)