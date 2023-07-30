import settings


class KeySet:
    class Key:
        def __init__(self, key_code: str, key):
            self._key_code = key_code
            self._key = key

        def get_code(self):
            return self._key_code

        def get_key(self):
            return self._key

        def set_key(self, key):
            self._key = key

    key_top = Key("top", None)

    key_right = Key("right", None)

    keys = [
        key_top,
        key_right
    ]

    def __init__(self, name: str, settings: settings.Settings):
        self._name = name
        self._settings = settings

    def _init_keys(self):
        key_dict = self._settings.get(self._name, self._settings.KeySet.KEY)
        for key in self.keys:
            pg_key = getattr(pygame, key_dict[key.get_code()])
            key.set_key(pg_key)
