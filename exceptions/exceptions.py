class GameException(Exception):
    """ The base game exception class """


class ConfigException(GameException):
    """ Configuration file exception """

    def __init__(self, msg):
        super().__init__("Configuration file: [ " + msg + " ]")


class ConfigNotFoundException(ConfigException):
    """ Configuration file not found """

    _msg = "file not found: {0}"

    def __init__(self, filename):
        super().__init__(self._msg.format(filename))


class ConfigJSONException(ConfigException):
    """ error reading JSON from config file """

    def __init__(self, msg):
        super().__init__(msg)


class ConfigKeyException(ConfigException):
    """ Missing key in configuration file """

    _msg = 'Missing key: "{0}"'

    def __init__(self, key):
        super().__init__(self._msg.format(key))
