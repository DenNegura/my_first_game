import tkinter as tk
from tkinter import ttk


class ScrollCanvas(ttk.Frame):

    def __init__(self, master, x_scroll: bool, y_scroll: bool, **kwargs):
        super().__init__(master, **kwargs)
        self._canvas = tk.Canvas(self)
        if x_scroll:
            self._init_x_scroll()

    def _init_x_scroll(self):
        self._scroll_x = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
