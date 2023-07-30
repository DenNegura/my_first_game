import json
from json import JSONDecodeError

from exceptions.exceptions import ConfigNotFoundException, ConfigJSONException, ConfigKeyException


class Settings:
    _instance = None

    CONFIG_PATH = "./config.json"

    LINK = "@"

    class Window:
        WINDOW_SIZE = ("window", "size")

    class Tile:
        SPRITE = "sprite"

        SIZE = "size"

        DELAY = "delay"

        SPRITE_POSITION = "position"

    class Actor:
        SPEED = "speed"

        STATE = "state"

    class KeySet:
        KEY = "key"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._open_config(self.CONFIG_PATH)

    def _open_config(self, path: str) -> None:
        try:
            with open(path) as f:
                self._config = json.load(f)
        except FileNotFoundError as e:
            raise ConfigNotFoundException(e.filename)
        except JSONDecodeError as e:
            raise ConfigJSONException(e.msg)

    def get(self, *args):
        args = self._flatten_box(args)
        config = self._config
        try:
            for constant in args:
                config = config[constant]
            if isinstance(config, list) and config[0] == Settings.LINK:
                config = self.get(*config[1:])
            return config
        except KeyError as e:
            raise ConfigKeyException(e.args[0])

    @staticmethod
    def _flatten_box(box):
        _box = []
        def flatten(item):
            if isinstance(item, tuple):
                for sub_item in item:
                    flatten(sub_item)
            else:
                _box.append(item)

        flatten(box)
        return tuple(_box)

