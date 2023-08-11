import tkinter as tk
from tkinter import ttk


class ScrollCanvas(ttk.Frame):

    def __init__(self, master, x_scroll: bool = True, y_scroll: bool = True, **kwargs):
        super().__init__(master, **kwargs)
        self._x_scroll = x_scroll
        self._y_scroll = y_scroll
        self._is_active_x_scroll = x_scroll
        self._is_active_y_scroll = y_scroll

        self._canvas = tk.Canvas(self)

        self._canvas.grid(row=0, column=0, sticky=tk.NSEW)

        if self._x_scroll:
            self._init_x_scroll()
            self._is_active_x_scroll = True
        if self._y_scroll:
            self._init_y_scroll()
            self._is_active_y_scroll = True

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.bind("<Configure>", self._resize)
        self._canvas.bind("<MouseWheel>", self._on_mouse_v_wheel)
        self._canvas.bind("<Control-MouseWheel>", self._on_mouse_h_wheel)

    def _init_x_scroll(self):
        self._scroll_x = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        self._canvas.config(xscrollcommand=self._scroll_x.set)
        self._scroll_x.config(command=self._canvas.xview)
        self._scroll_x.grid(row=1, column=0, sticky=tk.EW)

    def _init_y_scroll(self):
        self._scroll_y = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self._canvas.config(yscrollcommand=self._scroll_y.set)
        self._scroll_y.config(command=self._canvas.yview)
        self._scroll_y.grid(row=0, column=1, sticky=tk.NS)

    def _x_scroll_change_state(self):
        size = self._canvas.bbox(tk.ALL)
        y_scroll_size = 20 if self._is_active_y_scroll else 0

        if size is None or self.winfo_width() > size[2] + y_scroll_size:
            self._is_active_x_scroll = False
            self._scroll_x.grid_forget()
        else:
            self._is_active_x_scroll = True
            self._scroll_x.grid(row=1, column=0, sticky=tk.EW)

    def _y_scroll_change_status(self):
        size = self._canvas.bbox(tk.ALL)
        if size is None or self.winfo_height() > size[3]:
            self._is_active_y_scroll = False
            self._scroll_y.grid_forget()
        else:
            self._is_active_y_scroll = True
            self._scroll_y.grid(row=0, column=1, sticky=tk.NS)

    def _resize(self, event):
        if self._x_scroll:
            self._x_scroll_change_state()
        if self._y_scroll:
            self._y_scroll_change_status()
        region = self._canvas.bbox(tk.ALL)
        self._canvas.configure(scrollregion=region)

    def _on_mouse_v_wheel(self, event):
        if self._is_active_y_scroll:
            self._canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def _on_mouse_h_wheel(self, event):
        if self._is_active_x_scroll:
            self._canvas.xview_scroll(-1 * (event.delta // 120), "units")

    def get_canvas(self):
        return self._canvas
