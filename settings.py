import json
from json import JSONDecodeError

from exceptions.exceptions import ConfigNotFoundException, ConfigJSONException, ConfigKeyException


class Settings:
    _instance = None

    CONFIG_PATH = "./config.json"

    WINDOW_SIZE = (("window", "width"), ("window", "height"))

    SPRITES = "sprite"

    DIRECTION_TOP = ("direction", "top")

    DIRECTION_LEFT = ("direction", "left")

    DIRECTION_DOWN = ("direction", "down")

    DIRECTION_RIGHT = ("direction", "right")

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._open_config(self.CONFIG_PATH)

    def _open_config(self, path):
        try:
            with open(path) as f:
                self._config = json.load(f)
        except FileNotFoundError as e:
            raise ConfigNotFoundException(e.filename)
        except JSONDecodeError as e:
            raise ConfigJSONException(e.msg)

    def get(self, args):
        if type(args[0]) == tuple or type(args[0]) == list:
            return self.get_tuple(args)
        return self.get_constant(args)

    def get_constant(self, args: tuple | list):
        config = self._config
        try:
            for constant in args:
                config = config[constant]
            return config
        except KeyError as e:
            raise ConfigKeyException(e.args[0])

    def get_tuple(self, args_list: tuple[tuple] | list[tuple]):
        constants = []
        for args in args_list:
            constants.append(self.get(args))
        return tuple(constants)
