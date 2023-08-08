import tkinter as tk
from tkinter import ttk
from . import regex
import re


class Spinbox(ttk.Spinbox):

    def __init__(self, master, **kwargs):
        self._from = kwargs['from_']
        self._to = kwargs['to']
        super().__init__(master, **kwargs)

        self.configure(validate="key")
        self.configure(validatecommand=(self.register(self._validate), '%P'))

    def _validate(self, value):
        if value == "":
            return True
        return re.match(regex.NUMBER, value) is not None \
            and self._from <= float(value) <= self._to
