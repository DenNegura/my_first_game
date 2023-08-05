import tkinter as tk
from tkinter import ttk

root = tk.Tk()

frame = ttk.Frame(root)
frame.pack()

label1 = ttk.Label(frame, text="Label 1")
label1.pack()

label2 = ttk.Label(frame, text="Label 2")
label2.pack()

button = ttk.Button(frame, text="Button")
button.pack()

# Получаем список дочерних элементов фрейма
children = frame.winfo_children()

# Выводим информацию о дочерних элементах
for child in children:
    print(child)

root.mainloop()