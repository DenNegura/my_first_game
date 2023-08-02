import os.path
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from tiles_container import TilesContainer


class TileManager(ttk.Notebook):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._callback = None
        self._tile_containers = []

    def load_image(self, path_list: tuple[str] | list[str], tile_size: tuple[int, int] | list[int, int]):
        for path in path_list:
            print(path)
            if os.path.isfile(path):
                title = os.path.basename(path)
                id = self._get_id_by_title(title)
                if id is None:
                    self._create_tab(path, title, tile_size)
                else:
                    self.select(id)

    def _get_id_by_title(self, title) -> int | None:
        for id in range(self.index("end")):
            if self.tab(id, "text") == title:
                return id
        return None

    def _create_tab(self, path, title, tile_size):
        image = Image.open(path)
        container = TilesContainer(self, image, tile_size, self._on_select)
        container.pack(fill=tk.BOTH, expand=True)
        self.add(container, text=title)
        self._tile_containers.append(container)
        self.select(self.index("end") - 1)

    def _on_select(self, tile):
        pass