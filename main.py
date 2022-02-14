import pandas as pd

from src.PlotManager.BarPlot import show_bar
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

json = generate_json(repo_configuration)
commits_df = pd.read_json(json)

commits_peer_week = CommitsTimeline().get_commits_per_week(commits_df)

print(f"Project Name : {project_requested_name}")

commits_per_dev = (
    commits_df.groupby('name')
    .size()
    .to_frame('NumberOfCommits')
    .reset_index()
)

print(commits_per_dev)

show_bar(commits_peer_week)
