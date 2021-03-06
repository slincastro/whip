import unittest

from src.managers.projectManager import ProjectManager
from src.configuration.configuration import Configuration


class TestProjectManager(unittest.TestCase):

    def test_should_get_project_path_when_name_is_send(self):
        project_requested_name = 'AliquotNormalizationUI'
        configuration = Configuration("./test/test_app_config.yml")
        projectPath = ProjectManager(project_requested_name, configuration).get_project_path()

        print(projectPath)
        assert projectPath == "/path/To/Project"

    def test_should_get_project_path_service_when_name_is_send(self):
        project_requested_name = 'AliquotNormalizationService'
        configuration = Configuration("./test/test_app_config.yml")
        projectPath = ProjectManager(project_requested_name, configuration).get_project_path()

        print(projectPath)
        assert projectPath == "/path/To/ProjectService"

    def test_should_get_empty_project_path_when_non_existing_name_is_send(self):
        project_requested_name = 'AliquotNormalizationNonExisting'
        configuration = Configuration("./test/test_app_config.yml")
        projectPath = ProjectManager(project_requested_name, configuration).get_project_path()

        print(projectPath)
        assert projectPath == ""
