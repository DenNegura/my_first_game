import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
root = tk.Tk()
root.title("METANIT.COM")
root.geometry("250x200")

image = Image.open('C:/Projects/python/my_first_game/asserts/hero/sprite_sheet.png')

python_logo = ImageTk.PhotoImage(image=image)
# python_logo = tk.PhotoImage(file="C:/Projects/python/my_first_game/asserts/hero/sprite_sheet.png")

label = ttk.Label(image=python_logo)
label.pack()

root.mainloop()