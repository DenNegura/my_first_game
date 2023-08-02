import os.path
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk


class ImageLabel(ttk.Label):
    def __init__(self, master, pil_image: Image, callback, **kwargs):
        super().__init__(master, **kwargs)
        self._image = pil_image
        self._callback = callback
        self._tk_image = ImageTk.PhotoImage(self._image)
        self.config(image=self._tk_image)
        self.bind("<Button-1>", self._on_click)

    def _on_click(self):
        if self._callback:
            self._callback(self._image)


class TileManager(ttk.Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._callback = None
        self._width = None
        self._height = None

        # for test
        # self._width = 24
        # self._height = 32
        # self.load_image(image_path=['C:/Projects/python/my_first_game/asserts/hero/sprite_sheet.png'])

    def set_tile_size(self, width: int, height: int):
        self._width = width
        self._height = height

    def load_image(self, image_path):
        # todo нужен не список, о путь к файлу
        image_path = image_path[0]
        if os.path.isfile(image_path):
            image = Image.open(image_path)
            if self._width and self._height:
                self._load_image(image, self._width, self._height)

    def _load_image(self, image: Image, width: int, height: int) -> None:
        for x in range(image.width // width):
            for y in range(image.height // height):
                tile_image = image.crop((x * width, y * height, (x + 1) * width, (y + 1) * height))
                label = ImageLabel(master=self, pil_image=tile_image, callback=self.on_select)
                label.grid(row=y, column=x)

    def on_select(self, callback):
        self._callback = callback

    def _on_click(self):
        if self._callback:
            self._callback()
