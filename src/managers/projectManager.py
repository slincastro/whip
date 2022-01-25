class ProjectManager:
    def __init__(self, project, configuration):
        self.project = project
        self.configuration = configuration

    def get_project_path(self):
        project_path = self.project.split(".")
        path = self.configuration.get_configuration("projects")[project_path[0]][project_path[1]]["path"]
        return path

    def get_json_name(self):
        project_path = self.project.split(".")
        fileName = project_path[0] + ".json"
        return fileName

