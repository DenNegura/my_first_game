import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from Context import Context, ContextID
from ui.canvas.ScrollCanvas import ScrollCanvas


class TileList(ttk.Frame):

    def __init__(self, master, image: Image, tile_size: tuple[int, int] | list[int, int], **kwargs):
        super().__init__(master, **kwargs)
        self._width, self._height = tile_size
        self._image = image
        self._scroll_canvas = ScrollCanvas(master=self)
        self._scroll_canvas.pack(fill=tk.BOTH, expand=True)
        self._canvas = self._scroll_canvas.get_canvas()

        self._tiles = []
        self._context = Context()
        self.pack(fill=tk.X, expand=True)

        self._crop_image()
        self._draw_image()
        self.bind("<Configure>", self._resize)

    def _crop_image(self):
        for y in range(0, self._image.height, self._height):
            for x in range(0, self._image.width, self._width):
                tile = self._image.crop((x, y, x + self._width, y + self._height))
                image_tile = ImageTk.PhotoImage(tile)
                self._tiles.append((x, y, tile, image_tile))

    def _draw_image(self):
        for x, y, tile, image_tile in self._tiles:
            tile_id = self._canvas.create_image(x, y, anchor=tk.NW, image=image_tile)
            self._canvas.tag_bind(tile_id, "<Button-1>", lambda event, _tile=tile: self._on_change_tile(event, _tile))
        print(self._canvas.bbox(tk.ALL)[2] + 100)
        self.configure(width=self._canvas.bbox(tk.ALL)[2] + 100)

    def _on_change_tile(self, event, tile):
        self._context.send(tile, ContextID.TILE)

    def _resize(self, event):
        pass
        # print(self._canvas.bbox(tk.ALL)[2])
        # self.configure(width=self._canvas.bbox(tk.ALL)[2])
