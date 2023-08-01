import tkinter as tk
from tkinter import ttk


class GridController(ttk.LabelFrame):

    def __init__(self, master, canvas: tk.Canvas, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(text="Сетка")
        self._count_pixels = [(24, 24), (32, 32), (64, 64)]
        self._select_pixels = (32, 32)
        self._canvas = canvas
        self._is_drawn = False
        self._tags = ['line_grid']

    def _init_box(self):
        for sizes in self._count_pixels:
            rb = ttk.Radiobutton(text=lang, value=lang, variable=selected_language, command=_on_select)

        self._btn_grid = ttk.Button(self, text="Включить", command=self._on_click)
        self._btn_grid.pack(fill=tk.X)

    def _on_select(self):


    def _on_click(self):
        if self._canvas:
            if self._is_drawn:
                self._btn_grid.configure(text="Включить")
                self._delete_grid()
            else:
                self._btn_grid.configure(text="Выключить")
                self._draw_grid()

    def _delete_grid(self):
        for tag in self._tags:
            self._canvas.delete(tag)

    def _draw_grid(self):
        step_y, step_x = self._count_pixels
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        for y in range(step_y, height, step_y):
            self._canvas.create_line(0, y, width, y, tags=self._tags)
        for x in range(step_x, width, step_x):
            self._canvas.create_line(x, 0, x, height, tags=self._tags)
