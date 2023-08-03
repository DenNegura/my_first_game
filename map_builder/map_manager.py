from tkinter import ttk

from map_canvas import MapCanvas
from map_factory import MapFactory


class MapManager(ttk.Notebook):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._maps = []
        self._map_factory = MapFactory(self)
        self._map_factory.on_create_map(self._on_create_map)
        self._map_factory.pack(expand=True)
        self.add(self._map_factory, text="Home")

    def _on_create_map(self, map_size, tile_size):
        map = MapCanvas(self, map_size, tile_size)
        map.pack(expand=True)
        self.add(map, text="Map")
        self._maps.append(map)

