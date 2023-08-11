import tkinter as tk
from tkinter import ttk

from PIL import ImageTk

from Context import Context, ContextID
from Map import Map, Tile
from ui.canvas.ScrollCanvas import ScrollCanvas


class MapCanvas(ttk.Frame):

    _GRID_TAG = "grid"

    def __init__(self, master, map_size, tile_size, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._imagePil = None
        self._imageTk = None
        self._tile_x, self._tile_y = tile_size
        self._map_x = map_size[0] * self._tile_x
        self._map_y = map_size[1] * self._tile_y

        self._scroll_frame = ScrollCanvas(self)
        self._scroll_frame.pack(fill=tk.BOTH, expand=True)
        self._canvas = self._scroll_frame.get_canvas()
        self._create_grid()
        self._map = Map()

        self._context = Context()
        self._context.subscribe(self.set_tile, ContextID.TILE)

        # self._canvas.bind("<Configure>", self._resize)
        self._canvas.bind_all("<Control-z>", self._undo)
        self._canvas.bind("<Button-1>", self._on_draw_image)
        self._canvas.bind("<B1-Motion>", self._on_draw_image)

    def _create_grid(self):
        for y in range(0, self._map_y + self._tile_y, self._tile_y):
            self._canvas.create_line(0, y, self._map_x, y, tags=self._GRID_TAG)
        for x in range(0, self._map_x + self._tile_x, self._tile_x):
            self._canvas.create_line(x, 0, x, self._map_y, tags=self._GRID_TAG)

    def _on_draw_image(self, event):
        if self._imageTk:
            x, y = self._get_tile_position(event.x, event.y)
            if 0 <= x < self._map_x and 0 <= y < self._map_y:
                id = self._canvas.create_image(x, y, anchor=tk.NW, image=self._imageTk)
                last_tile = self._map.set(Tile(x, y, id, "", self._imagePil, self._imageTk))
                print(last_tile)
                if last_tile:
                    self._canvas.delete(last_tile.id)

    def _get_tile_position(self, x: int, y: int) -> tuple[int, int]:
        return x // self._tile_x * self._tile_x, y // self._tile_y * self._tile_y

    def set_tile(self, tile):
        self._imagePil = tile
        self._imageTk = ImageTk.PhotoImage(self._imagePil)

    # def _resize(self, event):
    #     print(event)
    #     print(self._scroll_frame.winfo_width())

    def _undo(self, event):
        tile = self._map.undo()
        if tile:
            self._canvas.delete(tile.id)
