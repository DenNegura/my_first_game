import tkinter as tk
from tkinter import ttk

from map_builder.view.MapGeneratorView import MapGeneratorView
from map_builder.map_canvas import MapCanvas


class MapManager(ttk.Notebook):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._maps = []
        self._map_factory = MapGeneratorView(self)
        self._map_factory.listen(self._on_create_map)
        self._map_factory.pack(expand=True)
        self.add(self._map_factory, text="Home")

        self._on_create_map({'width_map': 10, 'height_map': 10, 'width_tile': 32, 'height_tile': 32})

    def _on_create_map(self, values: dict):
        map_size = (values["width_map"], values["height_map"])
        tile_size = (values["width_tile"], values["height_tile"])
        map = MapCanvas(self, map_size, tile_size)
        map.pack(fill=tk.BOTH, expand=True)
        self.add(map, text="Map")
        self._maps.append(map)
        self.select(len(self._maps))

    def set_tile(self, tile):
        for map in self._maps:
            map.set_tile(tile)
