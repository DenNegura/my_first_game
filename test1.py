import tkinter as tk
from tkinter import ttk

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.scrollbar = ttk.Scrollbar(self, orient="vertical")
        self.scrollable_frame = tk.Text(self, yscrollcommand=self.scrollbar.set)

        self.scrollable_frame.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.scrollbar.config(command=self.scrollable_frame.yview)

root = tk.Tk()
scrollable_frame = ScrollableFrame(root)
scrollable_frame.pack(expand=True, fill="both")

for i in range(50):
    scrollable_frame.scrollable_frame.insert(tk.END, f"Label {i}\n")

root.mainloop()
