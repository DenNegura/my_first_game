import tkinter as tk
from tkinter import ttk


class MapManager(ttk.Notebook):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._init_home_tab()

    def _init_home_tab(self):
        self.add(container, text=title)
        self._tile_containers.append(container)

