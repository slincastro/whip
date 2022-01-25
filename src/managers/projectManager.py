from src.configuration.configuration import Configuration


class ProjectManager:
    def __init__(self, project):
        self.project = project

    def get_project_path(self):
        project_path = self.project.split(".")
        path = Configuration.get_configuration("projects")[project_path[0]][project_path[1]]["path"]
        return path

