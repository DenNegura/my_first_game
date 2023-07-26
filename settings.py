import json
from json import JSONDecodeError

from exceptions.exceptions import ConfigNotFoundException, ConfigJSONException, ConfigKeyException


class Settings:
    _instance = None

    CONFIG_PATH = "./config.json"

    class Window:
        WINDOW_SIZE = ("window", "size")

    class Tile:
        SPRITE = ("tile", "sprite")

        SIZE = ("tile", "size")

        DELAY = ("tile", "delay")

        SPRITE_POSITION = ("tile", "position")

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

    def get(self, *args) -> tuple:
        args = self._flatten_box(args)
        config = self._config
        try:
            for constant in args:
                config = config[constant]
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

    # def _get_constant(self, args) -> tuple:
    #     config = self._config
    #     try:
    #         for constant in args:
    #             config = config[constant]
    #         return config
    #     except KeyError as e:
    #         raise ConfigKeyException(e.args[0])

    # def _get_tuple_constants(self, args_list) -> tuple:
    #     constants = []
    #     for args in args_list:
    #         constants.append(self._get_constant(args))
    #     return tuple(constants)
    #
    # def _create_path(path: tuple | list, property: str) -> tuple:
    #     _path = []
    #     if type(path[0]) == tuple or type(path[0]) == list:
    #         for part_path in path:
    #             _part_path = list(part_path)
    #             _part_path.append(property)
    #             _path.append(_part_path)
    #     else:
    #         _path = list(path)
    #         _path.append(property)
    #     return tuple(_path)

