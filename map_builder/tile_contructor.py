import tkinter as tk
from tkinter import ttk
from ui.input.spinbox import Spinbox


class TileConfigurator(tk.Toplevel):

    def __init__(self, title, **kwargs):
        super().__init__(None, kwargs)
        self.title(title)
        self.geometry("200x200")
        self.grab_set()

        self._inner_frame = ttk.LabelFrame(self, text="Tile")
        self._inner_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self._width = tk.StringVar()
        self._height = tk.StringVar()
        self._is_default_value = tk.StringVar()
        self._is_default_value.set("0")

        ttk.Label(self._inner_frame, text="Width:")\
            .grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self._inner_frame, text="Height:")\
            .grid(row=1, column=0, padx=5, pady=5)

        Spinbox(self._inner_frame, width=8, from_=0, to=1000, textvariable=self._width)\
            .grid(row=0, column=1, padx=5, pady=5)
        Spinbox(self._inner_frame, width=8, from_=0, to=1000, textvariable=self._height)\
            .grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self._inner_frame, text="points")\
            .grid(row=0, column=2, padx=5, pady=5)
        ttk.Label(self._inner_frame, text="points")\
            .grid(row=1, column=2, padx=5, pady=5)

    def set_default_size(self, default_size, is_active):
        if is_active:
            self._is_default_value.set("1")
            self._width.set(str(default_size[0]))
            self._height.set(str(default_size[0]))
        ttk.Checkbutton(self._inner_frame, text="Use map sizes", variable=self._is_default_value) \
            .grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W)
