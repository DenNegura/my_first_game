import tkinter as tk

class CanvasExample:
    def __init__(self, master):
        self.master = master
        self.master.title("Canvas Example")

        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frame, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        for i in range(100):
            self.canvas.create_rectangle(0, i * 20, 20, (i + 1) * 20, fill="blue")

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        # Привязываем обработчики событий колесика мыши
        self.canvas.bind("<MouseWheel>", self._on_mouse_wheel)
        self.canvas.bind("<Button-4>", self._on_mouse_wheel)  # Прокрутка вверх
        self.canvas.bind("<Button-5>", self._on_mouse_wheel)  # Прокрутка вниз

    def _on_mouse_wheel(self, event):
        # Прокрутка холста при помощи колесика мыши
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

def main():
    root = tk.Tk()
    app = CanvasExample(root)
    root.mainloop()


main()
