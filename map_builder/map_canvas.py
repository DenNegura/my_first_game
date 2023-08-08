import tkinter as tk
from tkinter import ttk

from PIL import ImageTk

from map_builder.ui.canvas.ScrollCanvas import ScrollCanvas


class MapCanvas(ttk.Frame):

    _GRID_TAG = "grid"

    def __init__(self, master, map_size, tile_size, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._tile = None
        self._photo_tile = None
        self._scroll_frame = ScrollCanvas(self)
        self._scroll_frame.pack(fill=tk.BOTH, expand=True)
        self._canvas = self._scroll_frame.get_canvas()
        self._map_size = map_size
        self._tile_size = tile_size
        self._create_grid()

        self._canvas.bind("<Button-1>", self._on_draw_image)
        self._canvas.bind("<B1-Motion>", self._on_draw_image)

    def _create_grid(self):
        step_y, step_x = self._tile_size
        width = self._map_size[0] * step_x
        height = self._map_size[1] * step_y
        print(step_y, step_x)
        print(width, height)
        for y in range(0, height + step_y, step_y):
            self._canvas.create_line(0, y, width, y, tags=self._GRID_TAG)
        for x in range(0, width + step_x, step_x):
            self._canvas.create_line(x, 0, x, height, tags=self._GRID_TAG)

    def _on_draw_image(self, event):
        if self._photo_tile:
            x, y = self._get_rectangle_coord(event.x, event.y)
            if 0 <= x < self._map_size[0] * self._tile_size[0] and 0 <= y < self._map_size[1] * self._tile_size[1]:
                self._canvas.create_image(x, y, anchor=tk.NW, image=self._photo_tile)

    def _get_rectangle_coord(self, x: int, y: int) -> tuple[int, int]:
        x_size, y_size = self._tile_size
        return x // x_size * x_size, y // y_size * y_size

    def set_tile(self, tile):
        self._tile = tile
        self._photo_tile = ImageTk.PhotoImage(self._tile)
