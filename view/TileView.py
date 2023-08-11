import tkinter as tk
from tkinter import ttk

from ui.input.spinbox import Spinbox
from view.View import View


class TileView(View):

    def __init__(self, master, callback, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self._callback = callback

        self._inner_frame = ttk.LabelFrame(self, text="Tile")
        self._inner_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self._image_box = None
        self._image_inner_frame = None

        ttk.Label(self._inner_frame, text="Width:") \
            .grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self._inner_frame, text="Height:") \
            .grid(row=1, column=0, padx=5, pady=5)

        self._width = tk.StringVar()
        self._height = tk.StringVar()
        self._is_default_value = tk.StringVar()
        self._is_default_value.set("0")

        Spinbox(self._inner_frame, width=8, from_=0, to=1000, textvariable=self._width) \
            .grid(row=0, column=1, padx=5, pady=5)
        Spinbox(self._inner_frame, width=8, from_=0, to=1000, textvariable=self._height) \
            .grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self._inner_frame, text="points") \
            .grid(row=0, column=2, padx=5, pady=5)
        ttk.Label(self._inner_frame, text="points") \
            .grid(row=1, column=2, padx=5, pady=5)

        ttk.Button(self, text="Confirm", command=self._on_confirm)\
            .pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    def set_default_size(self, default_size):
        self._dict_values["map_size"] = default_size
        self._is_default_value.set("1")
        self._width.set(str(default_size[0]))
        self._height.set(str(default_size[0]))
        ttk.Checkbutton(self._inner_frame, text="Use map sizes", variable=self._is_default_value,
                        command=self._change_value) \
            .grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W)

    def _change_value(self):
        if self._is_default_value.get() == '0':
            self._width.set('')
            self._height.set('')
        else:
            map_size = self._dict_values["map_size"]
            self._width.set(map_size[0])
            self._height.set(map_size[1])

    def _on_confirm(self, event):
        if self._callback:
            self._dict_values["tile_width"] = int(self._width.get())
            self._dict_values["tile_height"] = int(self._width.get())
            self._callback(self._dict_values)