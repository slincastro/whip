import unittest

from src.managers.projectManager import ProjectManager


class TestProjectManager(unittest.TestCase):

    def test_should_get_project_path_when_name_is_send(self):
        project_requested_name = 'AliquotNormalization.chron'
        configuration = ProjectManager().get_project_path(project_requested_name)

        print(configuration)
        assert configuration == "/Users/slincastro/Projects/IDT/WinSvc-FormulationsOrderConverter"