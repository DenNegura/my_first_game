import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from settings import Settings


class MapBuilder(tk.Tk):
    def __init__(self):
        super().__init__()
        self._settings = Settings()
        self.title(self._settings.get(Settings.MapBuilder.CAPTION))
        size = self._settings.get(Settings.MapBuilder.WINDOW_SIZE)
        self.geometry(f'{size[0]}x{size[1]}')

        self._init_canvas()

        self._init_control_group()

        # Картинка, которую будем перемещать
        self.current_image = None
        self.current_image_id = None
        self.current_image_pos = (0, 0)

        # Картинки для объединения
        self.images_to_merge = []

    def _init_canvas(self):
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def _init_control_group(self):
        self.group_box = tk.Frame(self, width=1000)

        self.load_image_button = tk.Button(
            self.group_box, text="Выбрать картинку", command=self._load_image)
        self.load_image_button.pack(fill=tk.X)

        self.merge_button = tk.Button(
            self.group_box, text="Объединить картинки", command=self.merge_images)
        self.merge_button.pack(fill=tk.X)

        self.group_box.pack(fill=tk.X)

    def _load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            image = Image.open(file_path)
            # image.thumbnail((100, 100))  # Масштабируем картинку для удобства
            image = image.resize((2000, 2000))
            self.current_image = ImageTk.PhotoImage(image)
            self.current_image_id = self.canvas.create_image(0, 0, image=self.current_image, anchor=tk.NW)

            self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

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

    def merge_images(self):
        # Объединение картинок в одну большую картинку
        if self.images_to_merge:
            total_width = max(image.width for image in self.images_to_merge)
            total_height = sum(image.height for image in self.images_to_merge)

            merged_image = Image.new("RGB", (total_width, total_height), color="white")
            y_offset = 0
            for image in self.images_to_merge:
                merged_image.paste(image, (0, y_offset))
                y_offset += image.height

            # Сохраняем объединенную картинку
            merged_image.save("merged_image.jpg")

            # Очищаем холст и удаляем список картинок для объединения
            self.canvas.delete("all")
            self.images_to_merge = []


builder = MapBuilder()
builder.mainloop()
