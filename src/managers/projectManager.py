class ProjectManager:
    def __init__(self, project, configuration):
        self.project = project
        self.configuration = configuration

    def get_project_path(self):
        projects = self.configuration.get_configuration("projects")
        projects = map(lambda p: p["project"], projects)
        projects = filter(lambda p: p["name"] == self.project, projects)
        project = next(projects, {"path": ""})
        return project['path']
