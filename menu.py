import tkinter as tk
from tkinter import ttk

class Menu(tk.Menu):
    def __init__(self, master, **kwargs):
        super().__init__(master, kwargs)

        new_menu = tk.Menu()
        new_menu.add_command(label="Map")
        file_menu = tk.Menu()
        file_menu.add_command(label="New")

        self.add_cascade(label="File", menu=file_menu)