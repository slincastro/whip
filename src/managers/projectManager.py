import json


class ProjectManager:
    def __init__(self, project, configuration):
        self.project = project
        self.configuration = configuration

    def get_project_path(self):
        project_name = self.project.split(".")
        projects = self.configuration.get_configuration("projects")

        project = [x["project"] for x in projects if x["project"]["name"] == project_name[0]]

        return project[0]["path"]

    def get_json_name(self):
        project_path = self.project.split(".")
        fileName = project_path[0] + ".json"
        return fileName
