import tkinter as tk
from tkinter import ttk


class MapFactory(ttk.Frame):

    def __int__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._tile_size = ()
        self._tile_count = ()
        self._map_frame = ttk.LabelFrame(self, text="Map")
        self.l = ttk.Label(self._map_frame, text="label")
        self.l.pack(fill=tk.BOTH, expand=True)
        self._map_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self._tile_frame = ttk.LabelFrame(self, text="Tile")
        self._tile_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

