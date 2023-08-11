import os
import tkinter as tk
from tkinter import ttk

from PIL import Image

from Context import Context, ContextID
from component.tile.TileBuilder import TileBuilder
from component.tile.TileList import TileList


class TileBook(ttk.Notebook):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._tile_containers = []
        self._context = Context()
        self._context.subscribe(self.load_image, ContextID.SPRITE)

    def load_image(self, image_path):
        file_name = os.path.basename(image_path)
        image = Image.open(image_path)
        id = self._get_id_by_title(file_name)
        if id is None:
            TileBuilder(file_name, image, self._create_tab)
        else:
            self.select(id)

    def _get_id_by_title(self, title) -> int | None:
        for id in range(self.index("end")):
            if self.tab(id, "text") == title:
                return id
        return None

    def _create_tab(self, title, tile_size, image):
        container = TileList(self, image, tile_size)
        container.pack(fill=tk.BOTH, expand=True)
        self.add(container, text=title)
        self._tile_containers.append(container)
        self.select(self.index("end") - 1)
