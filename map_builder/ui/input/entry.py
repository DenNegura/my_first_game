import tkinter as tk
from tkinter import ttk
import re


class RegexEntry(ttk.Entry):

    def __init__(self, master, regex, **kwargs):
        super().__init__(master, **kwargs)
        self._regex = regex

        self.configure(validate="key")
        self.configure(validatecommand=(self.register(self._validate), '%P'))

    def _validate(self, value):
        return re.match(self._regex, value)
