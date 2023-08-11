import tkinter as tk
from tkinter import ttk

from ui.canvas.ScrollCanvas import ScrollCanvas


class ScrollFrame(ScrollCanvas):

    def __init__(self, master, x_scroll: bool = True, y_scroll: bool = True, **kwargs):
        super().__init__(master, x_scroll, y_scroll, **kwargs)


        self._inner_frame = ttk.Frame(self.get_canvas())

        self._frame_id = self._canvas.create_window((0, 0), window=self._inner_frame, anchor=tk.NW)


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
        if self.winfo_width() > self._inner_frame.winfo_width():
            self._scroll_x.grid_forget()
        else:
            self._scroll_x.grid(row=1, column=0, sticky=tk.EW)

    def _y_scroll_change_status(self):
        if self.winfo_height() > self._inner_frame.winfo_height():
            self._scroll_y.grid_forget()
        else:
            self._scroll_y.grid(row=0, column=1, sticky=tk.NS)

    def _resize(self, event):
        if self._x_scroll:
            self._x_scroll_change_state()
        if self._y_scroll:
            self._y_scroll_change_status()
        region = self._canvas.bbox(tk.ALL)
        self._canvas.configure(scrollregion=region)

    def _on_mouse_wheel(self, event):
        if event.state == 4:    # ctrl
            self._canvas.xview_scroll(-1 * (event.delta // 120), "units")
        else:
            self._canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def add(self, widget):
        widget.bind("<MouseWheel>", self._on_mouse_wheel)

    def get_master(self):
        return self._inner_frame
