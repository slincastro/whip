from src.configuration.configuration import Configuration


class ProjectManager:
    def get_project_path(self, project_name):
        project_path = project_name.split(".")
        path = Configuration.get_configuration("projects")[project_path[0]][project_path[1]]["path"]
        return path

