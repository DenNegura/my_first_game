import tkinter as tk
from tkinter import ttk

from map_factory import MapFactory


class MapManager(ttk.Notebook):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._map_factory = MapFactory(self)
        # self.label = ttk.Label(self, text="text")
        # self.label.pack(fill=tk.BOTH, expand=True)
        # self.add(self.label, text="label")
        self._init_map_factory()

    def _init_map_factory(self):
        self._map_factory.pack(fill=tk.BOTH, expand=True)
        self.add(self._map_factory, text="Home")

