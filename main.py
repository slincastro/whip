import pandas as pd
from src.configuration.configuration import Configuration
import subprocess

from src.filesManagers.json_manager import JsonManager
from src.managers.projectManager import ProjectManager

scriptPath = "./scripts/gitLogs.sh"
json_storage = Configuration.get_configuration("dataSource")
project_requested_name = 'AliquotNormalization.chron'
filename = "AliquotNormalization.json"

repo_configuration = ProjectManager(project_requested_name).get_project_path()
commits_file = json_storage + filename

subprocess.check_call(scriptPath + " %s %s" % (repo_configuration, commits_file), shell=True)

JsonManager().complete_json(commits_file)
data = pd.read_json(json_storage + filename)
dataAggregated = data.groupby('name').size()
print(dataAggregated)



