import pandas as pd
from configuration.configuration import Configuration
import subprocess

from filesManagers.json_manager import JsonManager

filename = "AliquotNormalization.json"
scriptPath = "./scripts/gitLogs.sh"
repo_configuration = Configuration.get_configuration("projects")["AliquotNormalization"]["chron"]["path"]
json_storage = Configuration.get_configuration("dataSource")
commits_file = json_storage + filename

subprocess.check_call(scriptPath + " %s %s" % (repo_configuration, commits_file), shell=True)

JsonManager().complete_json(commits_file)
data = pd.read_json(json_storage + filename)
dataAggregated = data.groupby('name').size()
print(dataAggregated)



