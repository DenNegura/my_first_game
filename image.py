import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageResizeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Resize App")
        self.geometry("800x600")

        # Создаем холст
        self.canvas = tk.Canvas(self, width=600, height=600, bg="white")
        self.canvas.pack(side=tk.LEFT)

        # Картинка, которую будем перемещать и увеличивать
        self.current_image = None
        self.current_image_id = None
        self.current_image_pos = (0, 0)
        self.current_image_scale = 1.0

        # Кнопка для выбора картинки
        self.load_image_button = tk.Button(self, text="Выбрать картинку", command=self.load_image)
        self.load_image_button.pack()

        # Привязываем обработчики событий клавиш
        self.bind("<KeyPress-Shift_L>", self.increase_size)
        self.bind("<KeyPress-Shift_R>", self.increase_size)

    def load_image(self):
        # Загрузка картинки и отображение на холсте
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file_path:
            image = Image.open(file_path)
            image.thumbnail((100, 100))  # Масштабируем картинку для удобства
            self.current_image = ImageTk.PhotoImage(image)
            self.current_image_id = self.canvas.create_image(0, 0, image=self.current_image, anchor=tk.NW)

            # Привязываем обработчики событий мыши для перемещения картинки
            self.canvas.tag_bind(self.current_image_id, "<ButtonPress-1>", self.start_drag)
            self.canvas.tag_bind(self.current_image_id, "<B1-Motion>", self.drag)

    def start_drag(self, event):
        # Начало перемещения картинки
        self.current_image_pos = (event.x, event.y)

    def drag(self, event):
        # Перемещение картинки по холсту
        dx = event.x - self.current_image_pos[0]
        dy = event.y - self.current_image_pos[1]
        self.canvas.move(self.current_image_id, dx, dy)
        self.current_image_pos = (event.x, event.y)

    def increase_size(self, event):
        # Увеличение размера картинки
        self.current_image_scale *= 1.2
        image = self.current_image._PhotoImage__photo.subsample(int(1 / self.current_image_scale))
        self.canvas.itemconfig(self.current_image_id, image=image)

app = ImageResizeApp()
app.mainloop()
