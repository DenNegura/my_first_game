from tkinter import ttk


class View(ttk.Frame):

    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._dict_values = {}
        self._callback = None

    def listen(self, callback):
        self._callback = callback

    def change(self):
        if self._callback:
            self._callback(self._dict_values)
