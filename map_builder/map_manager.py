import tkinter as tk
from tkinter import ttk

from map_factory import MapFactory


class MapManager(ttk.Notebook):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._map_factory = MapFactory(self)

        self._init_map_factory()

    def _init_map_factory(self):
        self.add(self._map_factory, text="Home")
        self._map_factory.pack(fill=tk.BOTH, expand=True)

