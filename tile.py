class Tile:

    TILE = "tile"

    SRITE = (TILE, "sprite")

    SIZE = ((TILE, "size", "width"), (TILE, "size", "height"))

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def path(self, path: tuple | list, property: str) -> tuple:
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

    def sprite(self) -> tuple:
        return self.path(self.SRITE, self._name)

    def size(self) -> tuple:
        return self.path(self.SIZE, self._name)