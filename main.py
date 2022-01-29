import matplotlib.pyplot as plt
import pandas as pd

from src.configuration.configuration import Configuration
from src.consoleDrawings.titles import display_title_bar
from src.filters.CommitsTimeLine import CommitsTimeline
from src.managers.json_manager import generate_json
from src.managers.projectManager import ProjectManager


display_title_bar()

project_requested_name = 'AliquotNormalizationWinService'

configuration = Configuration("app_config.yml")

project_manager = ProjectManager(project_requested_name, configuration)

repo_configuration = project_manager.get_project_path()
commits_file_path = project_manager.json_path

generate_json(repo_configuration, commits_file_path)

commitsDf = pd.read_json(commits_file_path)

commits_peer_week = CommitsTimeline().get_commits_per_week(commitsDf)

print(F"Project Name : {project_requested_name}")

commits_per_dev = commitsDf.groupby('name').size().to_frame('NumberOfCommits').reset_index()

print(commits_per_dev)

plt.bar(commits_peer_week["date"], height=commits_peer_week["NumberOfCommits"])

plt.show()

