import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk


class TilesContainer(ttk.Frame):

    def __init__(self, master, image: Image, tile_size: tuple[int, int] | list[int, int], callback, **kwargs):
        super().__init__(master, **kwargs)
        self._width, self._height = tile_size
        self._image = image
        self._canvas = tk.Canvas(master=self, bg="white")
        self._canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self._tiles = []
        self._callback = callback
        self.pack(fill=tk.BOTH, expand=True)

        self._crop_image()
        self._draw_image()
        self._init_scrollbars()

    def _init_scrollbars(self):
        v_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self._canvas.yview)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self._canvas.configure(yscrollcommand=v_scrollbar.set, scrollregion=self._canvas.bbox("all"))
        self._canvas.configure(width=self._image.width, height=self._image.height)

        self._canvas.bind("<MouseWheel>", self._on_mouse_wheel)
        self._canvas.bind("<Button-4>", self._on_mouse_wheel)
        self._canvas.bind("<Button-5>", self._on_mouse_wheel)

    def _crop_image(self):
        for y in range(0, self._image.height, self._height):
            for x in range(0, self._image.width, self._width):
                tile = self._image.crop((x, y, x + self._width, y + self._height))
                image_tile = ImageTk.PhotoImage(tile)
                self._tiles.append((x, y, tile, image_tile))

    def _draw_image(self):
        for x, y, tile, image_tile in self._tiles:
            tile_id = self._canvas.create_image(x, y, anchor=tk.NW, image=image_tile)
            self._canvas.tag_bind(tile_id, "<Button-1>", lambda event, _tile=tile: self._on_click(event, _tile))

    def _on_click(self, event, tile):
        self._callback(tile)

    def _on_mouse_wheel(self, event):
        self._canvas.yview_scroll(-1 * (event.delta // 120), "units")
