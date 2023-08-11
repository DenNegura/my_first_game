import os
import tkinter as tk
from tkinter import filedialog, ttk

from Context import Context


class FileExplorer(ttk.Frame):

    def __init__(self, master=None, extensions=(), **kwargs):
        super().__init__(master, **kwargs)

        self._button_select_dir = ttk.Button(self, text="open", command=self._select_directory)
        self._button_select_dir.pack(side=tk.TOP, fill=tk.X, expand=False, pady=5)
        self._callback_fun = None
        self._current_root_dir = None
        self._context = Context()
        self._accept_extensions = extensions
        self._init_explorer()

    def _init_explorer(self):
        self._tree = ttk.Treeview(self, show="tree")
        self._tree.heading("#0", text="Имя", anchor=tk.W)
        self._tree.column("#0", width=150)
        self._tree.bind("<<TreeviewSelect>>", self._on_select_item)

        self._tree.pack(expand=True, fill="both")

    def _add(self, parent, file_name, **kwargs) -> str:
        iid = parent + '/' + file_name if parent != "" else file_name
        return self._tree.insert(parent, "end", iid=iid, text=file_name, **kwargs)

    def _select_directory(self):
        def _read_inner_dir(directory):
            for file in os.listdir(directory):
                path_to_file = directory + '/' + file
                if os.path.isdir(path_to_file):
                    self._add(directory, file)
                    _read_inner_dir(path_to_file)
                else:
                    if self._is_accept_extension(file) is False:
                        continue
                    self._add(directory, file)

        directory_path = filedialog.askdirectory()
        if directory_path:
            if self._current_root_dir is not None:
                self._tree.delete(self._current_root_dir)
            self._current_root_dir = directory_path

            self._add("", directory_path, open=True)
            _read_inner_dir(directory_path)

    def _on_select_item(self, event):
        for selected_item in self._tree.selection():
            if os.path.isfile(selected_item):
                self._context.send(selected_item, Context.SPRITE)

    def on_select(self, callback_fun):
        self._callback_fun = callback_fun

    def set_extensions(self, extensions=list[str] | tuple[str]) -> None:
        self._accept_extensions = extensions

    def _is_accept_extension(self, file_name: str):
        for ext in self._accept_extensions:
            if file_name.endswith(ext):
                return True
        return False
