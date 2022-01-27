class ProjectManager:
    def __init__(self, project, configuration):
        self.project = project
        self.configuration = configuration
        self.json_name = self.get_json_name()
        self.json_path = self.get_json_path()

    def get_project_path(self):
        projects = self.configuration.get_configuration("projects")

        project = [x["project"] for x in projects if x["project"]["name"] == self.project]

        if len(project) == 0:
            return ""

        return project[0]["path"]

    def get_json_name(self):
        project_path = self.project.split(".")
        fileName = project_path[0] + ".json"
        return fileName

    def get_json_path(self):
        return F"{self.configuration.get_configuration('dataSource')}{self.json_name}"
