from game.tile import Tile


class MapTile:

    def __init__(self, x: int, y: int, id: int, tags: list[str] | str, tile: Tile):
        self.x, self.y, self.id = x, y, id
        if isinstance(tags, str):
            self.tag = [tags]
        else:
            self.tag = tags
        self.tile = tile

    def __str__(self):
        return f'MapTile:(x:{self.x}, y:{self.y}, id:{self.id}, tags:{self.tag})'


class History:

    ADD = 0

    REMOVE = 1
    def __init__(self):
        self._history = []



class Map:

    def __init__(self):
        self._map = {}
        self._history = []

    def set(self, tile: Tile) -> Tile | None:
        old_tile = self._set(tile)
        #self._history.append(tile)
        return old_tile

    def _set(self, tile: Tile) -> Tile | None:
        map = self._map.get(tile.x)
        if map:
            last_tile = map.get(tile.y)
            if last_tile:
                if last_tile != tile:
                    map[tile.y] = tile
                    self._history.append(last_tile)
                    return last_tile
            else:
                map[tile.y] = tile
        else:
            self._map[tile.x] = {tile.y: tile}
        # append empty
        # self._history.append(tile)
        self._history.append((tile.x, tile.y))
        return None

    def remove(self, x, y):
        remove_tile = self._remove(x, y)
        self._history.append(remove_tile)
        return remove_tile

    def _remove(self, x: int, y: int):
        y_map = self._map.get(x)
        if y_map:
            return y_map.pop(y, None)
        return None

    def undo(self) -> Tile | None:
        if self._history:
            tile = self._history.pop()
            return self._remove(tile.x, tile.y)
        return None
