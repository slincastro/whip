import unittest

from src.configuration.configuration import Configuration


class TestProjectManager(unittest.TestCase):

    def test_should_get_configuration(self):
        json_storage = Configuration("./test/test_app_config.yml").get_configuration("dataSource")
        print(json_storage)

        assert json_storage == "/path/to/json/"
