import tkinter as tk

from PIL import Image

from Context import Context, ContextID
from view.TileView import TileView


class TileBuilder(tk.Toplevel):

    def __init__(self, title, image: Image, callback, **kwargs):
        super().__init__(None, kwargs)

        self._title = title
        self._image = image
        self._callback = callback

        self.title(title)
        self.grab_set()
        self.resizable(width=False, height=False)

        self._context = Context()
        self._view = TileView(self, self._open_sprite)

        self._view.pack()

        self._tile_size = self._context.get(ContextID.MAP_SIZE)
        if self._tile_size:
            self._view.set_default_size(self._tile_size)

    def _open_sprite(self, values):
        if self._callback:
            tile_size = (values["tile_width"], values["tile_height"])
            self._callback(self._title, tile_size, self._image)
        self.destroy()
