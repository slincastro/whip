import subprocess

import matplotlib.pyplot as plt
import pandas as pd

from src.configuration.configuration import Configuration
from src.consoleDrawings.titles import display_title_bar
from src.filesManagers.json_manager import JsonManager
from src.managers.projectManager import ProjectManager

scriptPath = "./scripts/gitLogs.sh"
project_requested_name = 'AliquotNormalizationWinService'
display_title_bar()

configuration = Configuration("app_config.yml")

project_manager = ProjectManager(project_requested_name, configuration)

repo_configuration = project_manager.get_project_path()
commits_file_path = project_manager.json_path

subprocess.check_call(scriptPath + " %s %s" % (repo_configuration, commits_file_path), shell=True)

JsonManager().complete_json(commits_file_path)


commitsDf = pd.read_json(commits_file_path)
commitsDf['date'] = pd.to_datetime(commitsDf['date'], utc=True)
commitsDf = commitsDf.set_index(pd.DatetimeIndex(commitsDf['date']))

commits_by_month = commitsDf.resample('W').size().to_frame('NumberOfCommits').reset_index()

print(F"Project Name : {project_requested_name}")

commits_per_dev = commitsDf.groupby('name').size().to_frame('NumberOfCommits').reset_index()

print(commits_per_dev)

plt.bar(commits_by_month["date"], height=commits_by_month["NumberOfCommits"])

plt.show()

