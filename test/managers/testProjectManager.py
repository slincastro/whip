import unittest

from src.managers.projectManager import ProjectManager
from src.configuration.configuration import Configuration


class TestProjectManager(unittest.TestCase):

    def test_should_get_project_path_when_name_is_send(self):
        project_requested_name = 'AliquotNormalization.chron'
        configuration = Configuration("./test/test_app_config.yml")
        projectPath = ProjectManager(project_requested_name, configuration).get_project_path()

        print(projectPath)
        assert projectPath == "/path/To/Project"

    def test_should_return_json_object_name(self):
        project_requested_name = 'AliquotNormalization.chron'
        configuration = Configuration("./test/test_app_config.yml")
        jsonName = ProjectManager(project_requested_name, configuration).get_json_name()

        print(jsonName)
        assert jsonName == "AliquotNormalization.json"
