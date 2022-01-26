import pandas as pd
import subprocess
from src.configuration.configuration import Configuration
from src.filesManagers.json_manager import JsonManager
from src.managers.projectManager import ProjectManager

scriptPath = "./scripts/gitLogs.sh"
configuration = Configuration("app_config.yml")
json_storage = configuration.get_configuration("dataSource")
project_requested_name = 'AliquotNormalizationWinService.chron'

project_manager = ProjectManager(project_requested_name, configuration)

filename = project_manager.get_json_name()
repo_configuration = project_manager.get_project_path()
commits_file = json_storage + filename

subprocess.check_call(scriptPath + " %s %s" % (repo_configuration, commits_file), shell=True)

JsonManager().complete_json(commits_file)

data = pd.read_json(json_storage + filename)
dataAggregated = data.groupby('name').size()
print(dataAggregated)



