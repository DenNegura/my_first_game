class Tile:

    def __init__(self, path, x, y, imagePil, imageTk):
        self._path = path
        self._x = x
        self._y = y
        self._imagePil = imagePil
        self._imageTk = imageTk

    def __eq__(self, other: 'Tile'):
        return self._imageTk == other.get_image_tk()

    def get_image_pil(self):
        return self._imagePil

    def get_image_tk(self):
        return self._imageTk
