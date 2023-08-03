import tkinter as tk
from tkinter import ttk


class MapCanvas(tk.Canvas):

    _GRID_TAG = "grid"

    def __init__(self, master, map_size, tile_size, **kwargs):
        super().__init__(master, **kwargs)
        self._map_size = map_size
        self._tile_size = tile_size
        self._create_grid()

    def _create_grid(self):
        step_y, step_x = self._tile_size
        width, height = self._map_size
        for y in range(step_y, height, step_y):
            self.create_line(0, y, width, y, tags=self._GRID_TAG)
        for x in range(step_x, width, step_x):
            self.create_line(x, 0, x, height, tags=self._GRID_TAG)
