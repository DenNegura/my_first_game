import tkinter as tk

class ScrollableCanvasFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.yscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.yscrollbar.set)

        self.xscrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.configure(xscrollcommand=self.xscrollbar.set)

        self.inner_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        for i in range(100):
            tk.Label(self.inner_frame, text=f"Label {i}").pack()

        self.inner_frame.bind("<Configure>", self._configure_canvas)
        self.canvas.bind("<Configure>", self._configure_scrollregion)

    def _configure_canvas(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _configure_scrollregion(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

def main():
    root = tk.Tk()
    app = ScrollableCanvasFrame(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()
