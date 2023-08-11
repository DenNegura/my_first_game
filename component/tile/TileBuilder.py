import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from Context import Context, ContextID
from ui.input.spinbox import Spinbox
from view.TileView import TileView


class TileBuilder(tk.Toplevel):

    def __init__(self, title, image: Image, **kwargs):
        super().__init__(None, kwargs)
        self.title(title)
        self.grab_set()
        self.resizable(width=False, height=False)
        self._image = image
        self._context = Context()
        self._view = TileView(self, self._open_sprite)
        self._view.pack()

        self._tile_size = self._context.get(ContextID.MAP_SIZE)
        self._tile_size = (32, 32)  # todo remove line
        if self._tile_size:
            self._view.set_default_size(self._tile_size)

    def _open_sprite(self, values):
        pass