from tile import Tile
from settings import Settings

class Actor(Tile):

    def __init__(self, settings: Settings, name: str):
        super().__init__(settings, name)