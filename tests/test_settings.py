import unittest

from exceptions.exceptions import ConfigKeyException
from settings import Settings


class TestSettings(unittest.TestCase):
    _file_path = "./config.json"

    _correct_data = """
        {
          "window": {
            "width": 640,
            "height": 400
          }
        }
    """

    def create_file(self, values):
        try:
            with open(self._file_path, 'w') as file:
                file.write(values)
        except Exception as e:
            print(e)

    def test_shouldReturnWindowWidth(self):
        # Given
        self.create_file(self._correct_data)
        settings = Settings()
        args = "window", "width"
        width = 640

        # When
        data = settings.get(args)

        # Then
        self.assertEqual(data, width)

    def test_shouldReturnExceptionWhen(self):
        # Given
        self.create_file(self._correct_data)
        settings = Settings()
        args = "window", "empty"
        width = 640

        # When
        execution = lambda: settings.get(args)

        # Then
        self.assertRaises(ConfigKeyException, execution)
