import tkinter as tk
from tkinter import ttk


class MapBuilder(ttk.Frame):
    def __init__(self, master, tile_count: tuple[int, int] | list[int, int],
                 tile_size: tuple[int, int] | list[int, int], **kwargs):
        super().__init__(master, **kwargs)
        self._tags = {}
        self._tile_size = tile_size
        self._tile_count = tile_count
        self._canvas = tk.Canvas(master=self, bg="white")
        self._canvas.pack(fill=tk.BOTH, expand=True)

        self.create_grid()

    def create_grid(self):
        self._tags["grid"] = {"grid"}
        step_x, step_y = self._tile_size
        width = self._canvas.winfo_reqwidth()
        height = self._canvas.winfo_reqwidth()
        print(width, height)
        for y in range(step_y, height, step_y):
            self._canvas.create_line(0, y, width, y, tags=self._tags["grid"])
        for x in range(step_x, width, step_x):
            self._canvas.create_line(x, 0, x, height, tags=self._tags["grid"])