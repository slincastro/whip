import pandas as pd
from configuration.configuration import Configuration
import subprocess

filename = "AliquotNormalization"
repo_configuration = Configuration.get_configuration("projects")["AliquotNormalization"]["chron"]["path"]
json_storage = Configuration.get_configuration("dataSource")
command = "cd " + repo_configuration + "/ && git log" # --pretty=format:'{ \"name\": \"%aN\",\"email\": \"%aE\",\"date\": \"%aD\"},' >> /Users/slincastro/Projects/GitDataAnalisis/jsonData/OculusData.json"

#p = subprocess.Popen(["git","log","--pretty=format:'{ \"name\": \"%aN\",\"email\": \"%aE\",\"date\": \"%aD\"},' >> "+json_storage+filename+".json"], cwd=repo_configuration)
#p.wait()

#subprocess.Popen(["gitLogs.sh", json_storage+filename, repo_configuration], cwd=repo_configuration)

subprocess.check_call("./gitLogs.sh %s %s" % (json_storage, repo_configuration), shell=True)
#data = pd.read_json("/Users/slincastro/Projects/GitDataAnalisis/jsonData/OculusData.json")
#dataAggregated = data.groupby('email').size()
#print(dataAggregated)



