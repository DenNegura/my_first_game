import tkinter as tk
from tkinter import ttk


class MapFactory(ttk.Frame):
    _NUMBER_FROM = 1.0

    _NUMBER_TO = 100.0

    _PAD_X = 5

    _PAD_Y = 5

    _NUM_BOX_WIDTH = 8

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._callback = None

        self._inner_frame = ttk.LabelFrame(self, text="Create map")

        self._init_map_frame()
        self._init_tile_frame()
        self._init_button_frame()

        self._inner_frame.pack(expand=True)

    def _init_map_frame(self):
        self._frame_map = ttk.LabelFrame(self._inner_frame, text="Map")
        self._frame_map.grid(row=0, column=0, padx=self._PAD_X, pady=self._PAD_Y)

        self._create_label(parent=self._frame_map, text="Width:", pos=(0, 0))
        self._create_label(parent=self._frame_map, text="Height:", pos=(1, 0))

        self._width_map = tk.IntVar()
        self._height_map = tk.IntVar()
        self._entry_width_map = self._create_spinbox(parent=self._frame_map, pos=(0, 1), var=self._width_map)
        self._entry_height_map = self._create_spinbox(parent=self._frame_map, pos=(1, 1), var=self._height_map)

        self._create_label(parent=self._frame_map, text="tiles", pos=(0, 2))
        self._create_label(parent=self._frame_map, text="tiles", pos=(1, 2))

    def _init_tile_frame(self):
        self._frame_tile = ttk.LabelFrame(self._inner_frame, text="Tile")
        self._frame_tile.grid(row=0, column=1, padx=self._PAD_X, pady=self._PAD_Y)

        self._create_label(parent=self._frame_tile, text="Width:", pos=(0, 0))
        self._create_label(parent=self._frame_tile, text="Height:", pos=(1, 0))

        self._width_tile = tk.IntVar()
        self._height_tile = tk.IntVar()

        self._entry_width_tile = self._create_spinbox(parent=self._frame_tile, pos=(0, 1), var=self._width_tile)
        self._entry_height_tile = self._create_spinbox(parent=self._frame_tile, pos=(1, 1), var=self._height_tile)

        self._create_label(parent=self._frame_tile, text="points", pos=(0, 2))
        self._create_label(parent=self._frame_tile, text="points", pos=(1, 2))

    def _init_button_frame(self):
        self._create_button = ttk.Button(self._inner_frame,
                                         text="Create", state="disabled", command=self._create_map)
        self._create_button.grid(row=3, column=0, sticky=tk.W, padx=self._PAD_X, pady=self._PAD_Y)

    def _create_label(self, parent, text, pos):
        label = ttk.Label(parent, text=text)
        label.grid(row=pos[0], column=pos[1], padx=self._PAD_X, pady=self._PAD_Y)
        return label

    def _create_spinbox(self, parent, pos, var):
        validate_command = parent.register(self._num_validate)
        spinbox = ttk.Spinbox(parent, from_=self._NUMBER_FROM, to=self._NUMBER_TO,
                              width=self._NUM_BOX_WIDTH, textvariable=var)
        spinbox.configure(validate="key", validatecommand=(validate_command, "%P"))
        spinbox.grid(row=pos[0], column=pos[1], padx=self._PAD_X, pady=self._PAD_Y)
        spinbox.bind("<KeyRelease>", self._change_status_confirm_button)
        spinbox.bind("<<Increment>>", self._change_status_confirm_button)
        spinbox.bind("<<Decrement>>", self._change_status_confirm_button)
        return spinbox

    def _change_status_confirm_button(self, event):
        try:
            if self._width_map.get() and self._height_map.get() \
                    and self._width_tile.get() and self._height_tile.get():
                self._create_button.configure(state="normal")
            else:
                self._create_button.configure(state="disabled")
        except tk.TclError:
            pass

    def _create_map(self):
        if self._callback:
            self._callback((self._width_map.get(), self._height_map.get()),
                           (self._width_tile.get(), self._height_tile.get()))

    def on_create_map(self, callback):
        self._callback = callback

    @staticmethod
    def _num_validate(P):
        if P == "":
            return True
        try:
            float(P)
            return True
        except ValueError:
            return False
