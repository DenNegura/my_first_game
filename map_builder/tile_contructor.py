import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from ui.input.spinbox import Spinbox


class TileConfigurator(tk.Toplevel):

    def __init__(self, title, image: Image, **kwargs):
        super().__init__(None, kwargs)
        self.title(title)
        self.grab_set()

        self._inner_frame = ttk.LabelFrame(self, text="Tile")
        self._inner_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self._image_frame = ttk.LabelFrame(self, text="Image")
        self._image_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self._image = image

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


    def _print_image(self):
        self._canvas = tk.Canvas(self._image_frame)
        self._scroll_y = tk.Scrollbar(self._image_frame, orient="vertical", command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=self._scroll_y.set)
        self._scroll_y.pack(side="right", fill="y")
        self._canvas.pack(side="left", fill="both", expand=True)

        if self._image.width > 200:
            width_percent = (200 / float(self._image.size[0]))
            new_height = int((float(self._image.size[1]) * float(width_percent)))
            self._image = self._image.resize((200, new_height))
        self._image = ImageTk.PhotoImage(self._image)

        self._canvas.create_image(0, 0, anchor="nw", image=self._image)
        self._canvas.pack()
        self._canvas.bind("<Configure>", self._scroll_image)

    def _scroll_image(self, event):
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))

    def set_default_size(self, default_size, is_active):
        if is_active:
            self._is_default_value.set("1")
            self._width.set(str(default_size[0]))
            self._height.set(str(default_size[0]))
        ttk.Checkbutton(self._inner_frame, text="Use map sizes", variable=self._is_default_value) \
            .grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W)
