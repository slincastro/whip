import pandas as pd
from configuration.configuration import Configuration
import subprocess

filename = "AliquotNormalization.json"
repo_configuration = Configuration.get_configuration("projects")["AliquotNormalization"]["chron"]["path"]
json_storage = Configuration.get_configuration("dataSource")

subprocess.check_call("./scripts/gitLogs.sh %s %s" % (repo_configuration, json_storage+filename), shell=True)

#data = pd.read_json(json_storage + filename)
#dataAggregated = data.groupby('email').size()
#print(dataAggregated)



