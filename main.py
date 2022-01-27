import os
import matplotlib.pyplot as plt
import pandas as pd
import subprocess
from src.configuration.configuration import Configuration
from src.filesManagers.json_manager import JsonManager
from src.managers.projectManager import ProjectManager


def display_title_bar():
    os.system('clear')

    print("\t**********************************************")
    print("\t***  Let's - Review the project numbers!  ***")
    print("\t**********************************************")


display_title_bar()

scriptPath = "./scripts/gitLogs.sh"
configuration = Configuration("app_config.yml")
json_storage = configuration.get_configuration("dataSource")

project_requested_name = 'AliquotNormalizationWinService'

project_manager = ProjectManager(project_requested_name, configuration)

filename = project_manager.get_json_name()
repo_configuration = project_manager.get_project_path()
commits_file = json_storage + filename

subprocess.check_call(scriptPath + " %s %s" % (repo_configuration, commits_file), shell=True)

JsonManager().complete_json(commits_file)

commitsDf = pd.read_json(json_storage + filename)

commitsDf['date'] = pd.to_datetime(commitsDf['date'], utc=True)
commitsDf = commitsDf.set_index(pd.DatetimeIndex(commitsDf['date']))

resampleDf = commitsDf.resample('W').size().to_frame('NumberOfCommits').reset_index()

print("Project Name : " + project_requested_name)

dataAggregated = commitsDf.groupby('name').size().to_frame('NumberOfCommits').reset_index()

print(dataAggregated)

plt.bar(resampleDf["date"], height=resampleDf["NumberOfCommits"])

plt.show()

