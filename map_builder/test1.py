import tkinter as tk

root = tk.Tk()

paned_window = tk.PanedWindow(orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH, expand=True)

frame1 = tk.Frame(paned_window, width=100, height=200, bg="red")
frame2 = tk.Frame(paned_window, width=100, height=200, bg="blue")

paned_window.add(frame1)
paned_window.add(frame2)

root.mainloop()