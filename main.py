import pandas as pd

from src.PlotManager.BarPlot import *
from src.configuration.configuration import Configuration
from src.consoleDrawings.titles import display_title_bar
from src.filters.CommitsTimeLine import CommitsTimeline
from src.managers.json_manager import generate_json
from src.managers.projectManager import ProjectManager


display_title_bar()

project_requested_name = 'App-Personas'

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
    .sort_values(by=['NumberOfCommits'])
)

#print(commits_peer_week)
#print(commits_per_dev)
#show_bar_by_people(commits_per_dev, "name")
show_horizontal_bar(commits_per_dev)
#show_horizontal_commits_per_month(commits_peer_week)
#show_bar(commits_peer_week)
