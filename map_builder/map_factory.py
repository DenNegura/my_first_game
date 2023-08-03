import tkinter as tk
from tkinter import ttk


class MapFactory(ttk.Frame):

    def __int__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._tile_size = ()
        self._tile_count = ()
