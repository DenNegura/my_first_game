import tkinter as tk
from tkinter import filedialog, ttk

from PIL import Image, ImageTk

from file_explorer import FileExplorer
from grid_controller import GridController

from settings import Settings


class MapBuilder(tk.Tk):
    def __init__(self):
        super().__init__()
        self._settings = Settings()
        self.title(self._settings.get(Settings.MapBuilder.CAPTION))
        size = self._settings.get(Settings.MapBuilder.WINDOW_SIZE)
        self.geometry(f'{size[0]}x{size[1]}')

        # self._init_header_frame()

        self._panel = tk.PanedWindow(orient=tk.HORIZONTAL)

        self._explorer = self._init_explorer(self._panel)
        self._canvas = self._init_canvas(self._panel)

        self._panel.add(self._explorer)
        self._panel.add(self._canvas)

        self._panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self._init_control_group(self)

        # Картинка, которую будем перемещать
        self.current_image = None
        self.current_image_id = None
        self.current_image_pos = (0, 0)

        # Картинки для объединения
        self.images_to_merge = []

        self.bind("<KeyPress>", self._key_press)

    def _init_header_frame(self, master):
        self._header_frame = tk.Frame(master=master)
        self._header_frame.pack(side=tk.TOP, fill=tk.X)

    def _init_explorer(self, master) -> FileExplorer:
        explorer = FileExplorer(master=master, width=200)
        explorer.set_extensions((".png", ".jpg"))
        explorer.on_select(self._load_image)
        return explorer

    # def _load_image(self, file_path):
    #     #          self.image = Image.open(file_path)
    #     #         # image.thumbnail((100, 100))  # Масштабируем картинку для удобства
    #     #         # image = image.resize((2000, 2000))
    #     #
    #     #         self.current_image = ImageTk.PhotoImage(self.image)
    #     #         self.current_image_id = self.canvas.create_image(0, 0, image=self.current_image, anchor=tk.NW)
    #     print(file_path[0])
    #     image = Image.open(file_path[0])
    #     self._canvas.create_image(0, 0, image=ImageTk.PhotoImage(image=image), anchor=tk.NW)
    #     self._canvas.config(scrollregion=self._canvas.bbox(tk.ALL))

    def _init_canvas(self, master) -> tk.Canvas:
        canvas = tk.Canvas(master=master, bg="white")
        # canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        return canvas

    def _init_control_group(self, master):
        self.group_box = ttk.Frame(master=master)
        grid_component = GridController(self.group_box, self._canvas)

        grid_component.pack(fill=tk.X)
        self.group_box.pack(fill=tk.X)

    def _print_grid(self):
        step_x, step_y = 32, 32
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        for y in range(step_y, height, step_y):
            self._canvas.create_line(0, y, width, y, tags=['line_grid'])
        for x in range(step_x, width, step_x):
            self._canvas.create_line(x, 0, x, height, tags=['line_grid'])
        t = range(step_y, width, step_y)
        print(width)
        print(height)

    def _key_press(self, event):
        if event.keysym == "plus" and event.state == 1:  # 1 означает, что Shift нажат (event.state == 1)
            self.image = self.image.resize((self.image.width * 2, self.image.height * 2))
            self.current_image = ImageTk.PhotoImage(self.image)
            self.current_image_id = self._canvas.create_image(0, 0, image=self.current_image, anchor=tk.NW)
        if event.keysym == "underscore" and event.state == 1:
            print("state")
            self.image = self.image.resize((int(self.image.width / 2), int(self.image.height / 2)))
            self.current_image = ImageTk.PhotoImage(self.image)
            self.current_image_id = self._canvas.create_image(0, 0, image=self.current_image, anchor=tk.NW)

    def _load_image(self, file_path):
        # file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        file_path = file_path[0]
        if file_path:
            self.image = Image.open(file_path)
            # image.thumbnail((100, 100))  # Масштабируем картинку для удобства
            # image = image.resize((2000, 2000))

            self.current_image = ImageTk.PhotoImage(self.image)
            self.current_image_id = self._canvas.create_image(0, 0, image=self.current_image, anchor=tk.NW)

            self._canvas.config(scrollregion=self._canvas.bbox(tk.ALL))

            # Привязываем обработчики событий мыши для перемещения картинки
            self._canvas.tag_bind(self.current_image_id, "<ButtonPress-1>", self.start_drag)
            self._canvas.tag_bind(self.current_image_id, "<B1-Motion>", self.drag)

    def start_drag(self, event):
        # Начало перемещения картинки
        self.current_image_pos = (event.x, event.y)

    def drag(self, event):
        # Перемещение картинки по холсту
        dx = event.x - self.current_image_pos[0]
        dy = event.y - self.current_image_pos[1]
        self._canvas.move(self.current_image_id, dx, dy)
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
            self._canvas.delete("all")
            self.images_to_merge = []


builder = MapBuilder()
builder.mainloop()
