import pygame

import settings


class KeySet:
    class Key:
        def __init__(self, key_code: str):
            self._key_code = key_code
            self._key = None

        def get_code(self):
            return self._key_code

        def set_key(self, key):
            self._key = key

        def get_key(self):
            return self._key

    k_top = Key("top")

    k_right = Key("right")

    k_bottom = Key("bottom")

    k_left = Key("left")

    def __init__(self, name: str, settings: settings.Settings):
        self._name = name
        self._settings = settings
        self._init_keys()

    def _init_keys(self):
        key_dict = self._settings.get(self._name, self._settings.KeySet.KEY)
        for key in self._keys.keys():
            self._keys[key] = getattr(pygame, key_dict[key])

    def get(self, key_code: str):
        return self._keys[key_code]
