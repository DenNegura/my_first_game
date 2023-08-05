import tkinter as tk
from tkinter import ttk


class ScrollFrame(ttk.Frame):

    def __init__(self, master, x_scroll: bool = True, y_scroll: bool = True, **kwargs):
        super().__init__(master, **kwargs)
        self._x_scroll = x_scroll
        self._y_scroll = y_scroll

        self._canvas = tk.Canvas(self)
        self._inner_frame = ttk.Frame(self._canvas)

        self._canvas.create_window((0, 0), window=self._inner_frame, anchor=tk.NW)
        self._canvas.grid(row=0, column=0, sticky=tk.NSEW)

        if self._x_scroll:
            self._init_x_scroll()
            self._is_active_x_scroll = True
        if self._y_scroll:
            self._init_y_scroll()
            self._is_active_y_scroll = True

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.bind("<Configure>", self._resize)
        self._inner_frame.bind("<Configure>", self._resize)
        self._inner_frame.bind("<MouseWheel>", self._on_mouse_wheel)
        self._canvas.bind("<MouseWheel>", self._on_mouse_wheel)

    def _init_x_scroll(self):
        self._scroll_x = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        self._canvas.config(xscrollcommand=self._scroll_x.set)
        self._scroll_x.config(command=self._canvas.xview)
        self._scroll_x.grid(row=1, column=0, sticky=tk.EW)

    def _init_y_scroll(self):
        self._scroll_y = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self._canvas.config(yscrollcommand=self._scroll_y.set)
        self._scroll_y.config(command=self._canvas.yview)
        self._scroll_y.grid(row=0, column=1, sticky=tk.NS)

    def _x_scroll_change_state(self):
        if self.winfo_width() > self._inner_frame.winfo_width():
            self._scroll_x.grid_forget()
        else:
            self._scroll_x.grid(row=1, column=0, sticky=tk.EW)

    def _y_scroll_change_status(self):
        if self.winfo_height() > self._inner_frame.winfo_height():
            self._scroll_y.grid_forget()
        else:
            self._scroll_y.grid(row=0, column=1, sticky=tk.NS)

    def _resize(self, event):
        if self._x_scroll:
            self._x_scroll_change_state()
        if self._y_scroll:
            self._y_scroll_change_status()

        region = self._canvas.bbox(tk.ALL)
        self._canvas.configure(scrollregion=region)

    def _on_mouse_wheel(self, event):
        if event.state == 4:    # ctrl
            self._canvas.xview_scroll(-1 * (event.delta // 120), "units")
        else:
            self._canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def activate_scroll(self):
        for child in self._inner_frame.winfo_children():
            child.bind("<MouseWheel>", self._on_mouse_wheel)

    def get_frame(self):
        return self._inner_frame


tk_app = tk.Tk()
frame = ScrollFrame(tk_app)

b = None
image = None

def add():
    global image
    # b.destroy()
    image = tk.PhotoImage(file="C:/Projects/python/my_first_game/asserts/tiles_img.png")
    tk.Label(frame.get_frame(), image=image).pack()
    frame.activate_scroll()
add()
# b = ttk.Button(frame.get_frame(), text="add image", command=add)
# b.pack()

frame.activate_scroll()
frame.pack(expand=True, fill=tk.BOTH)
# frame.pack()
tk_app.mainloop()
